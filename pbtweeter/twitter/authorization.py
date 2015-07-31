import tweepy
import yaml


def authenticate(auth):
    file_load = raw_input('Attempt to use auth tokens in auth.yml? (Y/N):')
    if file_load.lower() in ['y', 'yes']:
        try:
            with open('../config/auth.yml', 'r') as f:
                tokens = yaml.load(f)
        except IOError:
            print "auth.yml doesn't exist."
            return
        else:
            auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
            return True
    elif file_load.lower() in ['n', 'no']:
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'
            return
        print 'Go to {}, authorize the application and retrieve the verification code'.format(redirect_url)
        verifier = raw_input('Input your verification code:')
        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            print 'Error! Failed to get access token.'
            return
        write = None
        while write is None:
            write = write_auth(auth)
        return True
    else:
        print 'Please enter Y (yes) or N (no)'
        return


def write_auth(auth):
    write = raw_input('Write tokens to auth.yml for future use? This wil overwrite existing tokens! (Y/N)')
    if write.lower() in ['y', 'yes']:
        with open('../config/auth.yml', 'w+') as f:
            yaml.dump({'access_token': str(auth.access_token), 'access_token_secret': str(auth.access_token_secret)},
                      f, default_flow_style=False)
            return True
    elif write.lower() in ['n', 'no']:
        return True
    else:
        print 'Please enter Y (yes) or N (no)'
    return


def get_api():

    keys = {}
    try:
        with open('../config/API.yml', 'r') as f:
            keys = yaml.load(f)
    except IOError:
        print "API.yml doesn't exist, please check the readme to find out how to create it"
        exit()

    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])

    authenticated = None
    while authenticated is None:
        authenticated = authenticate(auth)

    return tweepy.API(auth)
