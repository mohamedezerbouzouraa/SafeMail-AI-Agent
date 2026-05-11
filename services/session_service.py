from google.adk.sessions import InMemorySessionService

APP_NAME = "email_agent_app"
USER_ID = "user_001"
SESSION_ID = "email_session"

session_service = InMemorySessionService()
async def create_session():
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID)
