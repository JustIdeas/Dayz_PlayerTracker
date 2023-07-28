# Dayz_PlayerTracker
The Idea of this project was to improve the real time monitoring for INPUT and PLAYER  folders logs in the dayz server.

***INPUT Folder***
It contains (when configured in the server) the logs of each keyboard key stroke by any player, so the idea of this script is to get every INSERT or HOME key that was pressed from a user and log that in real time so that who is managing the server can see in real time and double check if the player is using any kind of hack. Remember that there is a need to configure that log to show at least those 2 keys to be logged in that folder

***PLAYER Folder***
That folder contains all players logs, and from those logs I check if there is any "killed by" String, and if that matches, it will also show in the terminal in real time. That helps if there is already some suspect of being using hack and that one just logged in and killed someone, so that the manager can access the server and take a closer look to that player.

So basically, in near future, I will allow the user of this program to also change those matching strings to be more dynamic on the search.

This is really basic because I don't have many experience of what is important to monitor in real time from all logs and files that a Dayz Server has, so any tips for sure would help :)

***About the program***

There is only one config.json file, that you need to configure changing the directory patch of where those INPUT and PLAYER folders are, so that the program can reado from it.
Also the program will look first to all logs files that are in those folders and show at first time, after reading the whole thing, it will show in real time every time that those log files are changed based on those filters explained at those topics at the top.
