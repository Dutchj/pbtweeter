import config as cfg
import loop
import os
import sys
from twitter import authorization

sys.path.append(os.path.dirname(__file__))

if __name__ == '__main__':

    api = None

    if not cfg.debug:
        api = authorization.get_api()

    loop.start(api)
