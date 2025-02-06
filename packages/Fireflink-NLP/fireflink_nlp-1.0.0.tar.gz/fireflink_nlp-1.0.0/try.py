from langchain_openai import ChatOpenAI
from Fireflink_NLP import Agent,Browser, BrowserConfig
import asyncio
from Fireflink_NLP import BrowserConfig
from Fireflink_NLP.browser.context import BrowserContext
async def run_agent():
    context = BrowserContext(browser=Browser(BrowserConfig(headless=False)))
    token = "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"

    agent = Agent(
        task="""Open Flipkart application on the browser \n Ensure internet connection is available,Enter valid email id and password in the login page {\"email\": \"test@gmail.com\", \"password\": \"password123\"} Click on 'Login' button""",
        use_vision=False,
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=token),
        browser_context=context
    )

    try:
        result = await agent.run()
        print(agent.resultstep)
    finally:
        await context.browser.close()  # Ensure the browser is closed properly

asyncio.run(run_agent())

        
