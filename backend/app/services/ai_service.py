import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_morning_brief(data):

    prompt = f"""
You are Rajan's Operations Intelligence Assistant.

Analyze the following operational data.

{data}

Return:

1. Critical Issues
2. Attention Required Today
3. Healthy Operations
4. Recommended Actions

Keep response concise.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content