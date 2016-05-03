
__all__ = ['Bot', 'run_bot']

from .bot import Bot
from aiohttp import web

def run_bot(bot_cls, host='localhost', port=None):
    app = web.Application()
    
    with bot_cls() as my_bot:
        app.router.add_route('POST', '/api', my_bot._handler)
        if __debug__:
            app.router.add_route('GET', '/history', my_bot._history)

        web.run_app(app, host, int(port))
