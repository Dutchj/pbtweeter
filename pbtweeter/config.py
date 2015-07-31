import os
import yaml

if not os.path.exists('../config/'):
        os.mkdir('../config/')
if not os.path.isfile('../config/config.yml'):
    default = {
        'Game': 'The Legend of Zelda: Ocarina of Time',
        'Interval': 60,
        'Data': '/data/',
        'Debug': False,

        'Categories': {'Any%': '20:00', '100%': '5:00:00'},

        'PB Messages': ['Congratulations to {player} for getting a {time} in {category}!',
                        '.{player} just got a {time} in {game} {category}!'],

        'WR Messages': ['A new World Record has been set for {category}! {time} by {player}!',
                        'WR Hype! {player} got a {time} for {game} {category}!'],

        'Tie Messages': ['The world record ({time}) for {category} has been tied by {player}!']
    }
    with open('../config/config.yml', 'w+') as f:
        yaml.safe_dump(default, f, default_flow_style=False)

try:
    with open('../config/config.yml', 'r') as f:
        settings = yaml.load(f)
except IOError:
    print "config.yml is missing"
    exit()
else:
    game = settings['Game']
    interval = settings['Interval']
    data_path = settings['Data']
    debug = settings['Debug']
    categories = settings['Categories']
    pb_messages = settings['PB Messages']
    wr_messages = settings['WR Messages']
    tie_messages = settings['Tie Messages']
