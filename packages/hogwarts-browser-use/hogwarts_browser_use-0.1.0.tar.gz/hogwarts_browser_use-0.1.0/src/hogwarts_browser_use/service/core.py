from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller
from langchain_core.language_models import BaseChatModel
from hogwarts_browser_use.model.task import Task


class HogwartsBrowserUse:
    def __init__(self, llm: BaseChatModel):
        self.llm = llm

    async def main(self, task: Task):
        controller = Controller()
        controller.registry.registry.actions.pop('search_google')
        # todo: 支持用户传递url
        browser = Browser(
            config=BrowserConfig(
                cdp_url="http://localhost:9222"
            )
        ) if task.reuse_browser else None
        agent = Agent(
            task=task.task,
            browser=browser,
            llm=self.llm,
            use_vision=False,
            controller=controller,
        )
        result = await agent.run()
        print(result.model_dump_json(indent=2))
