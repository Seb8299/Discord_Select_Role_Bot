# lion-turtle-role-gifter
> If you ask nicely the lion turtle will gift you with a role.

This is a simple discord role selection bot in the theme of a lion turtle, from the show Avatar: The Last Airbender, gifting users with an element (a customizable discord role).

## Find a Lion Turtle myself (hosting your own)
### Podman (Docker)
1. Make sure you have *podman* or *docker* installed
2. Clone or download and unzip the repository
3. Create a file called `config.json` in the projects root folder and enter `{ "token": "<my-token>"}` (make sure to replace `<my-token>` with your discord bot token)
4. Run `podman build -t lion-bot .`
5. Run `podman stop lion-bot`
6. Run `podman rm lion-bot`
7. Run `podman run -d --name lion-bot-container -it lion-bot`

### Manual
1. Make sure you have *python3* and *pip* installed
2. Clone or download and unzip the repository
3. Create a file called `config.json` in the projects root folder and enter `{ "token": "<my-token>"}` (make sure to replace `<my-token>` with your discord bot token)
4. Run `python3 -m pip install -U discord.py` (you maybe want to run it in a virtial enviroment)
5. Run `python3 main.py`

# Usage
1. Invite the bot to your server.
2. Run `/spawnTurtle`
3. Select your desired role
