# PremBot ⚽️ 🤖

An open source project to create a discord bot, which can provide comprehensive and live premier league data in a visual professional format.

## Project goals ☑️

Create a Discord bot which can provide live data about players and comparisons between them.

Create a library for easily accessing the data which is available at the fpl api.

## Features ⚙️

Below is a list of the full feature-set for the first version of the bot, this list may be amended based on restrictions of the data within the fpl api.

- [ ] matchday: provides a list of what premier league games are on the day which the command is called
- [ ] player [player1] : provides statistics on a player for the current premier league season
- [ ] table: provides the current status of the premier league (points and goal difference)
- [x] compare [player1] [player2] : compares some statistics between the two players listed
- [ ] topscorers [n | None] : provides the n highest scorers in the league during the current season (default is 5)
- [ ] topassisters [n | None] : provides the n highest assisters in the league during the current season (default is 5)

Suggestions for changes/additions to this list are welcome!

## Installation and usage ⬇️

1. Clone the repo `git clone https://github.com/OliverTansley/PremBot`
2. Ensure that you have pipenv installed on your machine `pip3 install pipenv`
3. Use `pipenv install` to install all the dependencies to a virtual environment
4. To run the bot `pipenv run python3 .` in the same directory as the `__main__.py` file

## Contributing 👨‍💻 👩‍💻

### Contributing Code

1. Follow the instructions above for how to install the codebase
2. Create a new branch for the intended feature `git branch feature-name`
3. Open a new pull request and wait for reviews and comments

### Contributing ideas

New ideas for features can be submitted by raising new issues for 'enhancement's
