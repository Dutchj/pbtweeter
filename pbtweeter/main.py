from twitter import authorization
import loop
import sys, os

sys.path.append(os.path.dirname(__file__))
    
if __name__ == '__main__':

    api = authorization.get_api()

    loop.start(api)
