from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv('./.env')
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

assistant = client.beta.assistants.create(
    name="IETEC Copilot Prototype",
    instructions="Você é o assistente virtual da startup Mnemoro...",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o",
)

def create_thread():
    return client.beta.threads.create()

def send_message(thread_id, prompt):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )
