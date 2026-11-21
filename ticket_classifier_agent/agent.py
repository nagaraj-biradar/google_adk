from typing import Literal
from google.adk.agents import Agent
from pydantic import BaseModel, Field

class Ticket(BaseModel):
    category: Literal["refund", "technical", "course_query", "payment", "others"] = Field(description= "The main topic of student's message.")
    urgency: Literal["low", "medium", "high"] = Field(description= "high = blocked right now or upset; medium = needs some help; low = general question ")
    needs_human : bool = Field(description= "True if human must handle this: money disputes, anger or anything unclear")

root_agent = Agent(
    name = "ticket_classifier",
    model='gemini-3.5-flash',
    description= "Classifies the support messages into ticket",
    instruction= """You classify the support messages sent by students. 
                    Read the message and fill in the ticket.  
                    Be conservative: If money, anger or confusion is involved, set needs_human to true.""",
    output_schema= Ticket,
    output_key= "ticket"                    
)
