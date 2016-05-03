from botframework import Bot, run_bot
import os

class SampleBot(Bot):
    pass

if __name__ == '__main__':
    run_bot(
        SampleBot,
        os.getenv('SERVER_HOST', 'localhost'),
        os.getenv('SERVER_PORT', None)
    )
