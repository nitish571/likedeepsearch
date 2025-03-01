import os
import gradio as gr
from dotenv import load_dotenv
from internal import perceive, reasoning

# Load environment variables from .env file
load_dotenv()

# API keys setup
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")  # Ensure this is set correctly

# Store research history
history = []

# Gradio interface
def research_agent(query):
    # perceive the query
    research_plan = perceive.process_query(query)
    # reason about the research plan and generates final plan
    final_response, memory_buffer = reasoning.reasoning_loop(query, research_plan)
    
    # Store query in history
    history.append({"query": query, "steps": memory_buffer})

    return final_response, history

interface = gr.Interface(
    fn=research_agent,
    inputs=gr.Textbox(lines=5, placeholder="Enter your research question here...", value="what is https://www.blackbox.ai/"),
    outputs=[
        gr.Textbox(label="Research Results"),
        gr.JSON(label="Research History")  # Shows all past queries & responses
    ],
    title="Deep Research Agent",
    description="An agent that uses reasoning to synthesize online information and complete multi-step research tasks."
)

interface.launch()
