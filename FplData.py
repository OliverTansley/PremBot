from typing import Any
from PIL import Image
import aiohttp


BASE_URL: str = 'https://fantasy.premierleague.com/api/'
PLAYER_ICONS_URL: str = 'https://resources.premierleague.com/premierleague/photos/players/110x140/p'


async def get_player(player_name: str) -> Any | None:
    '''
    returns the player json of a player with the name 'player_name'
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL+'bootstrap-static/') as response:
            fpl_request = await response.json()
            for player in fpl_request["elements"]:
                if player["web_name"].lower() == player_name.lower():
                    return player
    return None


async def get_player_image(player) -> Image.Image:
    '''
    return a players thumbnail image as a PIL Image
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(PLAYER_ICONS_URL + str(player['photo'])[0:len(str(player['photo']))-3] + "png") as response:
            image_data = await response.content.read()
            return Image.open(image_data)
