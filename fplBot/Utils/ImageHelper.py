from enum import IntEnum
from io import BytesIO
from typing import Text, Tuple
from PIL import Image, ImageDraw, ImageFont
import discord


_square_unit_size: int = 120
_padding: int = 4

# Neutrals
WHITE: Tuple[int, int, int] = (245, 245, 245)
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
BACKGROUND_LIGHT: Tuple[int, int, int] = WHITE
BACKGROUND_DARK: Tuple[int, int, int] = MID_GRAY

# Text Colors
TEXT_LIGHT: Tuple[int, int, int] = DARK_GRAY
TEXT_DARK: Tuple[int, int, int] = BLACK


class TextLevel(IntEnum):
    TOP = 2*_padding + 4
    MIDDLE = _square_unit_size/2 - 12
    BOTTOM = _square_unit_size - 38


def create_image(dimensions: Tuple[int, int]) -> Image.Image:
    '''
    returns image of size specified by standard units (_square_unit_size)
    '''
    new_img: Image.Image = Image.new(
        'RGBA', _grid_pos_2_img_coords(dimensions))
    new_img.paste(WHITE, (0, 0, new_img.size[0], new_img.size[1]))
    return new_img


def draw_square(orig_img: Image.Image, grid_start: Tuple[int, int], grid_end: Tuple[int, int], colour: Tuple[int, int, int]) -> None:
    '''
    place a square in the region specified by the four gird positions given
    '''
    orig_img_draw: ImageDraw.ImageDraw = ImageDraw.Draw(orig_img)
    square_start: Tuple[int, int] = _grid_pos_2_img_coords(grid_start)
    square_end: Tuple[int, int] = _grid_pos_2_img_coords(grid_end)
    orig_img_draw.rounded_rectangle(
        (square_start[0]+_padding,
         square_start[1]+_padding,
         square_start[0]+square_end[0]-_padding,
         square_start[1]+square_end[1]-_padding),
        radius=10, fill=colour)


def add_text(orig_img: Image.Image, grid_loc: Tuple[int, int], text: str, level: TextLevel = TextLevel.MIDDLE, hightlight_color: Tuple[int, int, int] = (-1, -1, -1), text_color: Tuple[int, int, int] = WHITE) -> None:
    '''
    writes text to a specified grid at a height specified by the level arg
    '''
    font = ImageFont.truetype("Roboto-Black.ttf", 30)
    orig_img_draw: ImageDraw.ImageDraw = ImageDraw.Draw(orig_img)
    text_coord: Tuple[int, int] = _grid_pos_2_img_coords(grid_loc)
    text_coord = (text_coord[0]+2*_padding,
                  text_coord[1] + int(level)-_padding)
    if hightlight_color != (-1, -1, -1):
        orig_img_draw.rounded_rectangle(
            (text_coord[0]-_padding/2,
             text_coord[1]-_padding/2,
             text_coord[0]+font.getlength(text)+_padding/2,
             text_coord[1]+30+_padding/2),
            radius=4, fill=hightlight_color)
    orig_img_draw.text(text_coord, text, font=font,
                       fill=text_color)


def image_2_discord_file(img: Image.Image) -> discord.File:
    img_bytesio = BytesIO()
    img.save(img_bytesio)
    # seek back to the beginning of the bytes else not all of the image file will be stored in the discord.File object
    img_bytesio.seek(0)
    return discord.File(img_bytesio)


def _grid_pos_2_img_coords(orig_tuple) -> Tuple[int, ...]:
    return tuple(element * _square_unit_size for element in orig_tuple)


if __name__ == "__main__":
    img = create_image((5, 1))
    draw_square(img, (0, 0), (2, 1), RED)
    add_text(img, (0, 0), "Test text here", level=TextLevel.TOP)
    add_text(img, (0, 0), "Test text here",
             level=TextLevel.MIDDLE, hightlight_color=BLUE, text_color=BLACK)
    add_text(img, (0, 0), "Test text here", level=TextLevel.BOTTOM)
    img.show()
