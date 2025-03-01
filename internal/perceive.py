from utils.utils import get_llm_response

def process_query(query):
    planning_prompt = f"""
    Given the research query: "{query}"
    
    Break this down into a sequence of few research steps maximum five that would be needed to thoroughly answer this query.
    Each step should be clear and actionable.
    
    Steps:
    """
    
    research_plan = get_llm_response(planning_prompt)
    return research_plan