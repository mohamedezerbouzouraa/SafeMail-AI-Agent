from google.genai import types
from runner.agent_runner import runner
from services.session_service import USER_ID, SESSION_ID

async def call_agent_async(email_text: str):
    content = types.Content(
        role="user",
        parts=[types.Part(text=email_text)])
    final_response = "No response."

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response = event.content.parts[0].text
            break

    print(final_response)
