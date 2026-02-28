from groq import Groq
import os
from dotenv import load_dotenv
from prompt_templates import email_prompt

load_dotenv()

client=Groq(
  api_key=os.getenv("GROQ_API_KEY")
)

def generate_email(context,tone):
  prompt= email_prompt(context,tone)
  response= client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user" , "content":prompt}],
    max_tokens=500
  )
  return response.choices[0].message.content
