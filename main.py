import asyncio
import nest_asyncio
from utils.async_runner import call_agent_async
from services.session_service import create_session

nest_asyncio.apply()
async def main():
    await create_session()
    await call_agent_async("""
Hi John,
Just a reminder that the project deadline is tomorrow.
Please send me the final report before 5 PM.

Best,
Sarah
""")

    await call_agent_async("""
🔥 YOU WON A FREE IPHONE!!!
Click here now to claim your prize!!!
""")

    await call_agent_async("""
Hey! Are we still on for dinner tonight?
""")

if __name__ == "__main__":
    asyncio.run(main())
