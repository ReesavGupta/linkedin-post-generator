from state import State
from evals.nodes import linkedin_expert_evaluation, devops_engineer_evaluation, genai_engineer_evaluation, backend_engineer_evaluation, hiring_manager_evaluation
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import interrupt



# Define the graph structure
graph = StateGraph(State)

# Start node: Interrupt to get user input
graph.add_node("linkedin_expert_eval",linkedin_expert_evaluation)
graph.add_node("devops_engineer_eval",devops_engineer_evaluation)
graph.add_node("genai_engineer_eval",genai_engineer_evaluation)
graph.add_node("backend_engineer_eval",backend_engineer_evaluation)
graph.add_node("hiring_manager_eval",hiring_manager_evaluation)






# Interupt Function after Evals is done :

async def interrupt_after_evals(state: State):
    
