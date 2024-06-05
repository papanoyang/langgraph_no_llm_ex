from . import BaseAgent

class Agent02(BaseAgent):
    
  def run_agent(self, state: dict):
    query = state.get('agent01_result')
    print(f"{self.name} Start:\n{query}")
    result = self.call_model(query)
    print(f"{self.name}'s Result:\n{result}")
    return {"agent02_result": result}