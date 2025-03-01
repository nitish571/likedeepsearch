import os
from dotenv import load_dotenv
from together import Together

# Load environment variables from .env file
load_dotenv()
os.environ["TOGETHER_API_KEY"] = os.getenv("TOGETHER_API_KEY")  # Ensure this is set in the environment

# Initialize the client for the language model

client = Together()

def get_llm_response(message):
    try:
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in getting response: {str(e)}"
