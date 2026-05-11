from google.adk.runners import Runner
from agents.email_agent import EmailAgent
from config.model_config import get_model
from services.session_service import session_service, APP_NAME

email_agent = EmailAgent(get_model())
runner = Runner(
    agent=email_agent,
    app_name=APP_NAME,
    session_service=session_service
)
