from abc import abstractmethod
from aiohttp import web, ClientSession

LUIS_ENDPOINT = 'https://example.com'

class Bot:
    '''Base class of your bot.

    You should implement the ``on_message`` function.
    
    Text may be parsed using ``parse``
    '''
    def __init__(self):
        self.conversations = {}
        self.history = []
        self._client = ClientSession()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_tb):
        self._client.close()

    def close(self):
        self._client.close()

    async def parse(self, text):
        async with self._client.post(
            LUIS_ENDPOINT,
            text.encode('utf-8'),
        ) as resp:
            data = await resp.json()
        
        # TODO: Extract relevant information from data
        return data

    @abstractmethod
    async def on_message(self, conversation, text):
        pass

    async def _handler(self, request):
        return web.Response(
            b"Not implemented",
        )

    async def _history(self, request):
        return web.Response(
            '\n'.join('<p>{!r}</p>'.format(h) for h in self.history).encode('utf-8')
        )
