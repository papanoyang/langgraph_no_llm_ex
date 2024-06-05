class BaseAgent:
  def __init__(self, name: str) -> None:
    self.name = name
  
  def call_model(self, prompt:str):
    return f"これは[{prompt}]の結果です。"