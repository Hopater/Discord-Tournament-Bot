# README.md
# Discord Tournament Bot

## Features
- Single-elimination tournament manager
- Automatic bracket generation
- Styled bracket image drawn with Pillow
- Hosted for free on Railway

## Setup
1. Clone repo and create `.env`:
```bash
echo "DISCORD_TOKEN=your_bot_token_here" > .env
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run locally (optional):
```bash
python bot.py
```

all commands:
🔢 Step	🧠 Command	🧍 Who Can Use	💬 Description
1️⃣	/start_tournament	Host only	Starts the tournament and allows players to join by reacting with ⚽
2️⃣	⚽ emoji reaction	All users	Players react to the bot's message with ⚽ to join the tournament
3️⃣	/start_bracket	Host only	Generates randomized 1v1 matchups and draws the first bracket image
4️⃣	/result <p1> <score1> <p2> <score2>	Host only	Submits a match result, advances the bracket, and sends the updated bracket
🖼️	(auto on start/result)	Bot	Sends bracket.png after generating or updating the bracket
🏁	(optional) /bracket	Anyone (optional)	Sends the current bracket image (can be added if needed)
