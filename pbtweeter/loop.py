import speedrun, lbdata
import config as cfg
import twitter.tweets as tweets
import time as t
import os
from datetime import datetime


def log(msg):
    print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), msg

def start(api):
    interval = int(cfg.interval)*60
    if not os.path.exists('..{path}'.format(path=cfg.data_path)):
        os.mkdir('..{path}'.format(path=cfg.data_path))
    if not os.path.exists('..{path}data.yml'.format(path=cfg.data_path)) or \
            not os.path.exists('..{path}old.yml'.format(path=cfg.data_path)):
        log('Initializing database...')
        lb = speedrun.get_lb()
        lbdata.create_data(lb)
        lbdata.write_old(lb)
        log('Done')

    while True:
        start_time = int(t.time())
        log('Starting tweet cycle...')
        log('Getting leaderboard data...')
        new = speedrun.get_lb()
        if new is None:
            print 'Leaderboards could not be retrieved'
        else:
            old = lbdata.read_old()
            log('Finding new times...')
            times = lbdata.get_times(old,new)
            if times is None:
                log('No new times.')
            else:
                update_old = True
                tweeted = lbdata.load_data()
                for category, runs in times.iteritems():
                    for player, time in runs.iteritems():
                        if player not in tweeted[category].keys() or time < tweeted[category][player]:
                            if tweets.post_tweet(api, old, category, player, time):
                                lbdata.update_data(tweeted, category, (player,time))
                            else:
                                update_old = False
                if update_old:
                    lbdata.write_old(new)

        log('Cycle complete, sleeping until next cycle...')
        time_left = interval - (int(t.time()) - start_time)
        t.sleep(time_left)
