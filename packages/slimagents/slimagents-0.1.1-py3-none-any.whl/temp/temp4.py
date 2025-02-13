from slimagents import Agent

agent = Agent(
    model="gemini/gemini-1.5-pro",
)

response = agent.run_sync("Who are you?")
print(response.value)

