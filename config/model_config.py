import google.generativeai as genai
from google.generativeai import GenerativeModel, GenerationConfig

genai.configure(api_key="YOUR_API_KEY")

AGENT_MODEL = "models/gemini-1.5-pro-latest"

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_LOW_AND_ABOVE",
    },
]

generate_content_config = GenerationConfig(
    temperature=0.3,
    max_output_tokens=800,
    top_p=0.9,
)

def get_model():
    return GenerativeModel(
        model_name=AGENT_MODEL,
        generation_config=generate_content_config,
        safety_settings=safety_settings,
    )
