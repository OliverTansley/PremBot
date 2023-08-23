from typing import Tuple
from PIL import Image, ImageDraw


_outer_square_unit_size: int = 80
_padding: int = 4


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
    orig_img_draw.rectangle(
        (square_coords[0]+_padding,
         square_coords[1]+_padding,
         square_coords[0]+square_coords[2]-_padding,
         square_coords[1]+square_coords[3]-_padding),
        colour)


def _grid_pos_2_img_coords(orig_tuple) -> Tuple[int, ...]:
    return tuple(element * _outer_square_unit_size for element in orig_tuple)


if __name__ == "__main__":
    img = create_image((3, 2))
    draw_square(img, (0, 0, 1, 1), (255, 0, 0))
    draw_square(img, (1, 0, 2, 2), (0, 255, 0))
    img.show()
