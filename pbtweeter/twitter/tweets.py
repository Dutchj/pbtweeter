import config as cfg
import random
import speedrun
from datetime import datetime
from seconds import seconds_to_time


def post_tweet(api, lb, cat, p, t):
    player_name = p
    twitter_handle = speedrun.get_twitter_handle(p)
    if twitter_handle is None:
        return
    if not twitter_handle == '':
        player_name = twitter_handle

    if t < int(lb[cfg.game][cat]['1']['time']):
        return post_wr_tweet(api, cat, player_name, t)
    elif t == int(lb[cfg.game][cat]['1']['time']):
        return post_tie_tweet(api, cat, player_name, t)
    else:
        return post_pb_tweet(api, cat, player_name, t)


def post_pb_tweet(api, cat, p, t):
    try:
        if not cfg.debug:
            api.update_status(status=random.choice(cfg.pb_messages).format(game=cfg.game, category=cat, player=p,
                                                                           time=seconds_to_time(t)))
    except Exception, e:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), e
    else:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), "Tweeted out {player}'s PB ({time}) in {category}".format(
            player=p, time=seconds_to_time(t), category=cat)
        if cfg.debug:
            return False
        return True


def post_wr_tweet(api, cat, p, t):
    try:
        if not cfg.debug:
            api.update_status(status=random.choice(cfg.wr_messages).format(game=cfg.game, category=cat, player=p,
                                                                           time=seconds_to_time(t)))
    except Exception, e:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), e
    else:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), "Tweeted out {player}'s WR ({time}) in {category}".format(
            player=p, time=seconds_to_time(t), category=cat)
        if cfg.debug:
            return False
        return True


def post_tie_tweet(api, cat, p, t):
    try:
        if not cfg.debug:
            api.update_status(status=random.choice(cfg.tie_messages).format(game=cfg.game, category=cat, player=p,
                                                                            time=seconds_to_time(t)))
    except Exception, e:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), e
    else:
        print datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), "Tweeted out {player}'s WR tie ({time}) in {category}"\
            .format(player=p, time=seconds_to_time(t), category=cat)
        if cfg.debug:
            return False
        return True
