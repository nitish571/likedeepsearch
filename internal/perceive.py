from utils.utils import get_llm_response

def process_query(query):
    """
    Generates a sequence of research steps to thoroughly answer a given research query.

    Args:
        query (str): The research query to be processed.

    Returns:
        str: A sequence of research steps to answer the query.

    Raises:
        Exception: If the get_llm_response function fails.

    Notes:
        This function relies on the get_llm_response function to generate the research plan.
        The research plan is generated based on a prompt that is constructed using the input query.

    Examples:
        >>> query = "What are the effects of climate change on global food production?"
        >>> research_plan = process_query(query)
        >>> print(research_plan)
    """
    
    planning_prompt = f"""
    Given the research query: "{query}"
    
    Break this down into a sequence of few research steps maximum five that would be needed to thoroughly answer this query.
    Each step should be clear and actionable.
    
    Steps:
    """
    
    research_plan = get_llm_response(planning_prompt)
    return research_plan