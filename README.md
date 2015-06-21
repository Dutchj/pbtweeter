# pbtweeter
This is fairly simple commandline bot that will read leaderboard information from speedrun.com, and tweet out new PBs at a set interval.

I'll add more detailed information on how to set it up later, but the important points are as follows:

1. You need to create an app on apps.twitter.com, and get your own consumer key/ consumer secret pair. These need to be filled in in the appropriate places in config/API.yml.
2. The settings will have to changed in order to correspond with the game that you want to use this for. Instructions are in the config.yml file.
3. Dependencies need to be installed, the external dependencies of this bot are Tweepy and Yaml
