from urllib2 import urlopen, quote
import config as cfg
import json
from datetime import datetime

def get_lb():
    try:
        response = urlopen('http://www.speedrun.com/api_records.php?amount=999&game='+quote(cfg.game))
        return json.load(response)
    except Exception, e:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), 'Error getting leaderboard data:', e
        return


def get_twitter_handle(user):
    try:
        response = urlopen('http://www.speedrun.com/api/v1/users?max=200&name='+user)
        users = json.load(response)
    except Exception, e:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), 'Error getting user search:', e
        return
    else:
        if users['data'] is []:
            print "Unable to retrieve Twitter handle: No data, user most likely doesn't exist"
            return ''
        for entry in users['data']:
            if entry['names']['international'].lower() == user.lower():
                identifier = entry['id']
                break
        else:
            print "Unable to retrieve Twitter handle: User doesn't exist"
            return ''
        try:
            response = urlopen('http://www.speedrun.com/api/v1/users/'+str(identifier))
        except Exception, e:
            print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), 'Error getting user data:', e
            return
        else:
            user_data = json.load(response)
            if user_data['data']['twitter'] is None:
                return ''
            twitter_link = user_data['data']['twitter']['uri']
            return '@' + twitter_link.replace('http://www.twitter.com/', '').replace('%40', '')
