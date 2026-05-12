class BaseAgent:
    async def run(self, *args, **kwargs):
        raise NotImplementedError
