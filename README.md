# TODO
 Update readme
- Setup github actions to keep this fork in sync with upstream automatically
- Auto update after a sync

Mokujin (v3.0) is a discord bot that fetches Tekken 7 frame data.  
It uses [discord.py](https://github.com/Rapptz/discord.py) v2.0b and is updated to use Python 3.10+.

The bot now has all the functionalities currently planned. It seems to work well and is somewhat stable. Currently, the data the bot uses is being updated to Tekken 7 Season 4, and any further update will be added either on request or when we see a mistake.

Frame data is acquired from RBNorway, Geppopotamus, Tekken.guru, frame data feature (Tekken 7 DLC) and community members.


## If you want to use this:

Clone this to a linux server that has Python 3.10.0+ and install the dependencies with:
```py
pip install -r requirements.txt
```
 
You need your own discord bot ([instructions](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)) and have the tokens in the `src/resources/config.json`. You can add a feedback channel there also.


The executable is `src/mokujin.py`.

Commands:
```
Slash Command
/fd <character> <move>       -    get frame data of a move from a character
/last-updates         -    get the messages of some latest updates
/feedback <message>      -    send message to the author   

Direct ping
@discordbot <character> <move>        -    get frame data of a move from a character
```
