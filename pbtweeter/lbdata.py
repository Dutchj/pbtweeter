import config as cfg
import yaml
from seconds import time_to_seconds


def find_differences(old, new):
    game = cfg.game
    empty = True
    res = {}
    for category in cfg.categories.keys():
        times = {run['player']: int(run['time']) for run in new[game][category].values() if
                 run not in old[game][category].values()}
        if times:
            empty = False
            res[category] = times
    if empty:
        return
    return res


def find_old_times(new_times, old):
    res = {}
    for category in new_times:
        res[category] = {}
        players = new_times[category].keys()
        for run in old[cfg.game][category].values():
            if run['player'] in players:
                if run['player'] not in res[category].keys() or (run['player'] in res[category].keys()
                                                                 and int(run['time']) < res[category][run['player']]):
                    res[category][run['player']] = int(run['time'])
    return res


def get_times(old, new):
    res = {}
    new_times = find_differences(old, new)
    if new_times is None:
        return
    old_times = find_old_times(new_times, old)
    for category, times in new_times.iteritems():
        res[category] = {player: time for player, time in times.iteritems() if (
                         player not in old_times[category].keys() or
                         old_times[category][player] > time) and
                         time < time_to_seconds(cfg.categories[category])}
    return res


def create_data(lb):
    data = {}
    with open('..{path}data.yml'.format(path=cfg.data_path), 'w+') as f:
        for category, runs in lb[cfg.game].iteritems():
            data[category] = {run['player']: int(run['time']) for run in runs.values()}
        yaml.safe_dump(data, f, default_flow_style=False)


def load_data():
    with open('..{path}data.yml'.format(path=cfg.data_path), 'r') as f:
        data = yaml.load(f)
        return data


def update_data(data, category, time):
    data[category][time[0]] = time[1]
    with open('..{path}data.yml'.format(path=cfg.data_path), 'w+') as f:
        yaml.safe_dump(data, f, default_flow_style=False)


def read_old():
    with open('..{path}old.yml'.format(path=cfg.data_path)) as f:
        return yaml.load(f)


def write_old(old):
    with open('..{path}old.yml'.format(path=cfg.data_path), 'w+') as f:
        yaml.safe_dump(old, f, default_flow_style=False)


def read_new():
    with open('..{path}new.yml'.format(path=cfg.data_path)) as f:
        return yaml.load(f)


def write_new(new):
    with open('..{path}new.yml'.format(path=cfg.data_path), 'w+') as f:
        yaml.safe_dump(new, f, default_flow_style=False)