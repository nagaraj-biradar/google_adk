from datetime import datetime
from zoneinfo import ZoneInfoNotFoundError

from google.adk import Agent
from dotenv import load_dotenv

load_dotenv()

def get_current_time(timezone: str) -> dict:
    """Get the current time and date for a given time zone. Use this to answer when the user asks for the date & time. 
    
    Args: An IANA time zone name (e.g. Mumbai -> "Asia/Kolkata", "America/New York", "Europe/London")

    Return: A dict with "status" ("Success" or "Error"), On success it should have "timezone", "time", "date", "weekday".
    On error it should have error message.
    """
    try:
        now = datetime.now()
    except ZoneInfoNotFoundError:
        return {
            "status": "error",
            "error_message": f"Unknow time zone '{timezone}'"
        }
    return {
        "status": "success",
        "timezone": timezone,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M"),
        "weekday": now.strftime("%A")
    }
    

root_agent = Agent(
    name= "root_agent",
    model="gemini-3.6-flash",
    description="Tells the current time and date anywhere in the world",
    instruction="You tell the current time and date to the use. Translate the place name into IANA time zones yourself (e.g:Mumbai -> Asia/Kolkata and call get_current_time tool. If it returns error explain the promble to the user. )",
    tools= [get_current_time],
)
