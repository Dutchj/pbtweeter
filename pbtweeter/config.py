import yaml

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
    categories = settings['Categories']
    pb_messages = settings['PB Messages']
    wr_messages = settings['WR Messages']
    tie_messages = settings['Tie Messages']
