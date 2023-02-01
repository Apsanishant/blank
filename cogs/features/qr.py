import discord
from discord.ext import commands
from discord import app_commands
from colorama import Back, Fore, Style
import time
import qrcode
from io import BytesIO

class qr(commands.Cog):
     def __init__(self, client: commands.Bot):
        self.client = client
    
     @app_commands.command(name="qr", description="Generates A Qr Code")
     async def ping(self,interaction:discord.Integration, text:str):
       qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
       qr.add_data(text)
       qr.make(fit=True)
       img = qr.make_image(fill_color="black", back_color="white")
       buffer = BytesIO()
       img.save(buffer, "PNG")
       buffer.seek(0)
       await interaction.response.send_message(file=discord.File(fp=buffer, filename='qr_code.png'))
       prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE+Style.BRIGHT)
       print(prfx + " Qr Command Was Executed Successfully")

async def setup(client:commands.Bot) ->None:
    await client.add_cog(qr(client))
