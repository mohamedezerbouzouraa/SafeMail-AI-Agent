from agents.base_agent import BaseAgent

class EmailAgent(BaseAgent):
    def __init__(self, model):
        self.model = model

    async def run(self, user_id, session_id, message):
        prompt = f"""
You are an AI Email Assistant.

Your tasks:
1. Classify the email into:
   - Work
   - Personal
   - Spam

2. Summarize the email in 1-2 sentences.

3. Suggest a professional reply.

EMAIL:
{message.parts[0].text}

Return format:
Category:
Summary:
Suggested Reply:
"""

        response = self.model.generate_content(prompt)

        class Event:
            def is_final_response(self): return True
            @property
            def content(self):
                class Content:
                    @property
                    def parts(self):
                        class Part:
                            text = response.text
                        return [Part()]
                return Content()

        yield Event()
