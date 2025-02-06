import datetime as dt
from enum import IntEnum, StrEnum
from pathlib import Path
from typing import Literal
from uuid import UUID

from fastapi import FastAPI
from loguru import logger
from pydantic import UUID4, BaseModel, EmailStr, Field, HttpUrl, field_serializer
from pydantic_ai import Agent, RunContext

from knd.ai import user_message
from knd.memory import AgentMemories
from knd.memory import memorize as _memorize

IDEAL_CANDIDATE_AGENT_NAME = "ideal_candidate_agent"
RESUME_AGENT_NAME = "resume_agent"
MEMORIES_DIR = Path("memories")


IDEAL_CANDIDATE_PROMPT = """
You are a technical recruiter with expertise in creating candidate profiles. Your task is to create an ideal candidate profile in a specific format based on the job description provided.

Important Guidelines:
1. Use the job description to fill in all relevant fields
2. For fields not explicitly mentioned in the job description:
   - Fill in reasonable values if they can be confidently inferred from the context
   - Example: If job says "senior position" but no years specified, assume 7+ years
   - Example: If location mentions "hybrid in NYC", include NYC in location field
   - Example: If role is about python web development but does not mention FastAPI, add FastAPI to skills
3. Use industry standards and context to fill gaps:
   - Match skills with typical years of experience for the level
   - Include relevant certifications common in the field
   - Add typical projects someone in this role would have
4. Leave fields empty (use default values) if they cannot be reasonably inferred
   - For contact info like linkedin/github/portfolio, only include if specified in job description
5. Ensure all dates are logical and recent
6. Include achievements that would be impressive for this role
""".strip()

RESUME_PROMPT = """
You are a resume information extractor. Your task is to extract information from the resume provided and return it in a structured format.
""".strip()


class EducationLevel(IntEnum):
    HIGH_SCHOOL = 1
    ASSOCIATES = 2
    BACHELORS = 3
    MASTERS = 4
    PHD = 5
    OTHER = 0


class EmploymentType(StrEnum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"
    OTHER = "other"


class Skill(BaseModel):
    name: str
    level: int | None = Field(None, ge=1, le=10)
    years_experience: float | None = None


class Education(BaseModel):
    institution: str
    degree: str = ""
    level: EducationLevel
    field_of_study: str = ""
    gpa: float | None = Field(None, ge=0, le=4.0)
    description: str = ""
    start_date: dt.date | None = None
    end_date: dt.date | None = None


class WorkExperience(BaseModel):
    company: str
    title: str
    employment_type: EmploymentType
    location: str = ""
    is_current: bool = False
    description: str
    achievements: list[str] = Field(default_factory=list)
    start_date: dt.date | None = None
    end_date: dt.date | None = None


class Project(BaseModel):
    name: str
    description: str
    duties: list[str] = Field(default_factory=list)
    company: str = Field(
        "",
        description="The candidate may or may not have been an employee of this company, but the project was done for or with this company",
    )
    links: list[HttpUrl] = Field(default_factory=list)


class ContactInfo(BaseModel):
    email: EmailStr
    phone: str = ""
    location: str = ""
    linkedin: HttpUrl | None = None
    github: HttpUrl | None = None
    portfolio: HttpUrl | None = None


class Resume(BaseModel):
    years_of_experience: float

    summary: str = Field(description="Name and other personal information should not be included")

    work_experience: list[WorkExperience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    skills: list[Skill] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)

    last_updated: dt.date = Field(default_factory=dt.date.today)
    availability_date: dt.date | None = None


app = FastAPI()

dummy_resume = Resume(years_of_experience=10, summary="This is a dummy resume")

ideal_candidate_agent = Agent(
    model="openai:gpt-4o-mini",
    result_type=Resume,
    system_prompt=IDEAL_CANDIDATE_PROMPT,
    deps_type=AgentMemories,
    name=IDEAL_CANDIDATE_AGENT_NAME,
)
resume_agent = Agent(
    model="openai:gpt-4o-mini",
    result_type=Resume,
    system_prompt=RESUME_PROMPT,
    deps_type=AgentMemories,
    name=RESUME_AGENT_NAME,
)
memory_agent = Agent(model="google-gla:gemini-1.5-flash", name="memory_agent")


@ideal_candidate_agent.system_prompt(dynamic=True)
@resume_agent.system_prompt(dynamic=True)
def system_prompt(ctx: RunContext[AgentMemories]) -> str:
    logger.info(f"Adding dynamic agent experience: {ctx.deps}")
    return str(ctx.deps)


agents_dict = {IDEAL_CANDIDATE_AGENT_NAME: ideal_candidate_agent, RESUME_AGENT_NAME: resume_agent}


class AgentRequest(BaseModel):
    user_prompt: str
    agent_name: Literal["ideal_candidate_agent", "resume_agent"]
    user_id: UUID4 | str
    memorize: bool = True
    memories_dir: Path | str = MEMORIES_DIR

    @field_serializer("user_id")
    def serialize_user_id(self, v: UUID | str | None) -> str | None:
        return str(v) if v else None

    @field_serializer("memories_dir")
    def serialize_memories_dir(self, v: Path | str | None) -> str | None:
        return str(v) if v else None


@app.post("/run_agent")
async def run_agent(agent_request: AgentRequest) -> Resume:
    agent = agents_dict[agent_request.agent_name]
    memories = AgentMemories.load(
        agent_name=agent_request.agent_name or "agent",
        user_id=agent_request.user_id,
        memories_dir=agent_request.memories_dir,
        include_profile=False,
    )
    logger.info(f"Running agent: {agent.name} with memories: {memories.model_dump_json(indent=2)}")
    run = await agent.run(
        user_prompt=agent_request.user_prompt, deps=memories, message_history=memories.message_history
    )
    if agent_request.memorize:
        await _memorize(
            memory_agent=memory_agent,
            agent_memories=memories,
            message_history=run.all_messages(),
            new_messages=run.new_messages(),
            memories_dir=agent_request.memories_dir,
            user_id=memories.user_id or agent_request.user_id,
            include_profile=False,
        )
    return run.data


@app.put("/add_message")
async def add_user_message(add_message_request: AgentRequest) -> str:
    memories = AgentMemories.load(
        agent_name=add_message_request.agent_name,
        user_id=add_message_request.user_id,
        memories_dir=add_message_request.memories_dir,
    )
    memories.add_message(
        message=user_message(add_message_request.user_prompt), user_id=add_message_request.user_id
    )
    memories.dump(
        agent_dir=Path(add_message_request.memories_dir).joinpath(add_message_request.agent_name),
        user_id=add_message_request.user_id,
    )
    return "Message added successfully"
