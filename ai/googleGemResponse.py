import google.generativeai as gem
from google import genai
from google.genai import types
import os
client = genai.C(api_key="GEMINI_API_KEY")


API_KEY = os.environ['GOOGLE_GEM_API_KEY']
PROJECT_ID = os.environ['GOOGLE_GEM_PROJECT_ID']
model = "gemini-1.5-pro"

response = client.models.generate_content(
    model = model,
    contents = ["Explain how AI works"],
    config = types.GenerateContentConfig(
        max_output_tokens = 500,
        temperature = 0.1
    )
)