import json5 as json
from langgraph.graph import StateGraph, END

from agents import Agent01, Agent02, Agent03
from memory import AgentState

class TestAgentManger:
  def __init__(self) -> None:
    pass

  def run_workflow(self):
    agent01 = Agent01(name='Agent01')
    agent02 = Agent02(name='Agent02')
    agent03 = Agent03(name='Agent03')

    workflow = StateGraph(AgentState)

    workflow.add_node('agent01', agent01.run_agent)
    workflow.add_node('agent02', agent02.run_agent)
    workflow.add_node('agent03', agent03.run_agent)

    workflow.add_edge('agent01', 'agent02')
    workflow.add_edge('agent02', 'agent03')
    workflow.add_edge('agent03', END)

    workflow.set_entry_point('agent01')

    team = workflow.compile()

    result = team.invoke({"query": "Agent Workflow!"})

    print(json.dumps(result, indent=2, ensure_ascii=False))