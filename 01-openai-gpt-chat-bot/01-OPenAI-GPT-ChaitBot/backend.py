from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def ask_gpt(input):
    response = client.responses.create(
        model="gpt-6-astra",
        input=input
    )
    print(response)
    return response.output_text