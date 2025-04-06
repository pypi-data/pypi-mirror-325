from slimagents import Agent

agent = Agent(
    instructions="Your task is to convert PDF files to Markdown.",
    model="gemini/gemini-2.0-flash",
)

# response = agent.run_sync("Who are you?")
# print(response.value)

with open("./temp/Enchiladas med salat.pdf", "rb") as f:
    response = agent.run_sync(f)
    print(response.value)



# def foo(a, b, c=3, /, *, d):
#     print(a, b, c)

# foo(1, 2, 3)