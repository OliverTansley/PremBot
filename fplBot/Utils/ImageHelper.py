from enum import Enum
from io import BytesIO
from typing import Tuple
from PIL import Image, ImageDraw
import discord


_outer_square_unit_size: int = 80
_padding: int = 4

# Neutrals
SOFT_WHITE: Tuple[int, int, int] = (245, 245, 245)
LIGHT_GRAY: Tuple[int, int, int] = (200, 200, 200)
MID_GRAY: Tuple[int, int, int] = (150, 150, 150)
DARK_GRAY: Tuple[int, int, int] = (100, 100, 100)
BLACK: Tuple[int, int, int] = (0, 0, 0)

# Primary Colors
RED: Tuple[int, int, int] = (219, 68, 55)
GREEN: Tuple[int, int, int] = (15, 157, 88)
BLUE: Tuple[int, int, int] = (66, 133, 244)

# Accent Colors
ORANGE: Tuple[int, int, int] = (255, 149, 0)
YELLOW: Tuple[int, int, int] = (255, 204, 0)
PURPLE: Tuple[int, int, int] = (155, 89, 182)

# Complementary Colors
TEAL: Tuple[int, int, int] = (0, 150, 136)
PINK: Tuple[int, int, int] = (233, 30, 99)

# Subdued Colors
LIGHT_BLUE: Tuple[int, int, int] = (173, 216, 230)
LIGHT_GREEN: Tuple[int, int, int] = (144, 238, 144)
LIGHT_PURPLE: Tuple[int, int, int] = (216, 191, 216)

# Background Colors
BACKGROUND_LIGHT: Tuple[int, int, int] = SOFT_WHITE
BACKGROUND_DARK: Tuple[int, int, int] = MID_GRAY

# Text Colors
TEXT_LIGHT: Tuple[int, int, int] = DARK_GRAY
TEXT_DARK: Tuple[int, int, int] = BLACK


class TextLevel(Enum):
    TOP = 0
    MIDDLE = 10
    BOTTOM = 100


def create_image(dimensions: Tuple[int, int]) -> Image.Image:
    '''
    returns image of size specified by standard units (_outer_square_unit_size)
    '''
    return Image.new('RGBA', _grid_pos_2_img_coords(dimensions))


def draw_square(orig_img: Image.Image, grid_pos: Tuple[int, int, int, int], colour: Tuple[int, int, int]) -> None:
    '''
    place a square in the region specified by the four gird positions given
    '''
    orig_img_draw: ImageDraw.ImageDraw = ImageDraw.Draw(orig_img)
    square_coords: Tuple[int, int, int, int] = _grid_pos_2_img_coords(grid_pos)
    orig_img_draw.rounded_rectangle(
        (square_coords[0]+_padding,
         square_coords[1]+_padding,
         square_coords[0]+square_coords[2]-_padding,
         square_coords[1]+square_coords[3]-_padding),
        radius=20, fill=colour)


def image_2_discord_file(img: Image.Image) -> discord.File:
    img_bytesio = BytesIO()
    img.save(img_bytesio)
    # seek back to the beginning of the bytes else not all of the image file will be stored in the discord.File object
    img_bytesio.seek(0)
    return discord.File(img_bytesio)


def _grid_pos_2_img_coords(orig_tuple) -> Tuple[int, ...]:
    return tuple(element * _outer_square_unit_size for element in orig_tuple)


if __name__ == "__main__":
    img = create_image((3, 2))
    draw_square(img, (0, 0, 1, 1), colour=BLUE)
    draw_square(img, (1, 0, 2, 2), PURPLE)
    img.show()
