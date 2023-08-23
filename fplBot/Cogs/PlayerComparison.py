from typing import Any
from discord.ext import commands
import discord
import io
import FplData
from PIL import Image, ImageFont, ImageDraw


class PlayerComparison(commands.Cog):

    def __init__(self, bot: discord.Client) -> None:
        self.bot: discord.Client = bot

    @commands.command()
    async def goals(self, ctx: commands.Context, *args, member: discord.Member | discord.User | None = None):
        '''
        display image of player and their goals this season
        '''
        player = await FplData.get_player(args[0].lower())
        image_byteIo = io.BytesIO()
        player_image = await FplData.get_player_image(player)
        player_image.save(image_byteIo, "PNG")
        # Set file-pointer back to beginning so all bytes are read into discord.File()
        image_byteIo.seek(0)
        await ctx.send(file=discord.File(image_byteIo))
        await ctx.send(f'goals scored this season: {player["goals_scored"]}')

    @commands.command()
    async def compare(self, ctx: commands.Context, *args, member: discord.Member | discord.User | None = None) -> None:
        '''
        Display image showcasing player comparison of players ability
        '''
        player1 = await FplData.get_player(args[0])
        player2 = await FplData.get_player(args[1])
        compare_graphic = Image.new('RGBA', (400, 500), (255, 255, 255))
        compare_graphic.paste(await FplData.get_player_image(player1), (0, 0))
        compare_graphic.paste(await FplData.get_player_image(player2), (200, 0))
        self.paste_statistic(
            compare_graphic, "minutes", 300, player1, player2)
        self.paste_statistic(
            compare_graphic, "goals_scored", 350, player1, player2)
        self.paste_statistic(
            compare_graphic, "assists", 400, player1, player2)
        self.paste_statistic(
            compare_graphic, "points_per_game", 450, player1, player2)
        image_byteIo = io.BytesIO()
        compare_graphic.save(image_byteIo, "PNG")
        image_byteIo.seek(0)
        await ctx.send(file=discord.File(image_byteIo, filename=f'{args[0]}_{args[1]}_compared.png'))

    def paste_statistic(self, compare_thumbnail: Image.Image, statistic: str, level: int, player1, player2) -> None:
        '''
        adds necessary text to showcase statistic of two players
        '''
        font = ImageFont.truetype("Roboto-BoldItalic.ttf", 32)
        image_writer: ImageDraw.ImageDraw = ImageDraw.Draw(compare_thumbnail)
        image_writer.text((8, level), str(
            player1[statistic]), fill=(0, 0, 0), font=font)
        image_writer.text((400 - 16*len(str(
            player2[statistic])) - 8, level), str(
            player2[statistic]), fill=(0, 0, 0), font=font)
        image_writer.text((200-8*len(statistic), level), statistic.replace("_", " "),
                          fill=(0, 0, 0), font=font,)
