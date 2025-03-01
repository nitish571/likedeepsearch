from utils.utils import get_llm_response
from crewai_tools import SerperDevTool

# Initialize search tool
search_tool = SerperDevTool(n_results=5)

def reasoning_loop(query, research_plan):
    memory_buffer = []
    
    memory_buffer.append(f"Research Plan: {research_plan}")
    
    steps = [step.strip() for step in research_plan.split("\n") if step.strip()]
    
    for i, step in enumerate(steps):
        search_prompt = f"""
        Based on the research query: "{query}"
        And the current research step: "{step}"
        
        Formulate a specific search query to gather information for this step. Do not make the query lengthy concise it. 
        """
        
        search_query = get_llm_response(search_prompt)
        
        try:
            search_results = search_tool.run(search_query=search_query)
        except Exception as e:
            return f"Error in performing search: {str(e)}"
        
        synthesis_prompt = f"""
        Research query: "{query}"
        Current research step: "{step}"
        
        Based on the following search results:
        {search_results}
        
        And considering what we already know:
        {memory_buffer}
        
        Provide a concise synthesis of the information relevant to this research step.
        """
        
        step_synthesis = get_llm_response(synthesis_prompt)
        memory_buffer.append(f"Step {i+1} - {step}: {step_synthesis}")
    
    final_synthesis_prompt = f"""
    Research query: "{query}"
    
    Based on all the information gathered through our research steps:
    {memory_buffer}
    
    Provide a comprehensive answer to the original research query. The response should be well-structured,
    thorough, and directly address all aspects of the query.
    """
    
    final_response = get_llm_response(final_synthesis_prompt)
    
    return final_response, memory_buffer
