import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
from langchain_tavily import TavilySearch

load_dotenv()




llm = ChatDeepSeek(model="deepseek-flash", api_key=os.getenv("DEEPSEEK_API_KEY"))
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="search for 3 job postings for an devops , aws , platform engineer in the uae on linkedin and list their details")]}
    )
    print(result)


if __name__ == "__main__":
    main()
