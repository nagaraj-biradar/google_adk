from typing import Literal
from google.adk.agents import Agent
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class Enquiry(BaseModel):
    name: str | None = Field(default=None, description="Student's full name, properly capitalized")
    email: str | None = Field(default=None, description="Email address exactly as written")
    interested_in: list[Literal["GenAI", "Data Science", "MLOps", "Deep Learning", "Other"]] = Field(
        description="CampusX courses the student is interested in"
    )
    budget_inr: int | None = Field(default=None, ge=0, le=500000,
        description="Total budget in rupees as a plain number. Convert '15k' to 15000")

root_agent = Agent(
    name="enquiry_agent",
    model='gemini-3.5-flash',
    description="Extract students imformation from the message",
    instruction="Read student message and extract their details.",
    output_schema= Enquiry
)
