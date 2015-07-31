from twitter import authorization
import loop
import sys
import os
import config as cfg

sys.path.append(os.path.dirname(__file__))

if __name__ == '__main__':

    api = None

    if not cfg.debug:
        api = authorization.get_api()

    loop.start(api)
