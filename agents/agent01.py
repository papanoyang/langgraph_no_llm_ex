from . import BaseAgent

class Agent01(BaseAgent):
    
  def run_agent(self, state: dict):
    query = state.get('query')
    print(f"{self.name} Start:\n{query}")
    result = self.call_model(query)
    print(f"{self.name}'s Result:\n{result}")
    return {"agent01_result": result}