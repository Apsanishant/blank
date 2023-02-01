import discord
from discord.ext import commands
from discord import app_commands

class ban(commands.Cog):
     def __init__(self, client: commands.Bot):
        self.client = client
    
     @app_commands.command(name="ban", description="Ban A User")
     async def ping(self,interaction:discord.Integration, member:discord.Member, reason:str):
        await member.send(f"You Were Banned from {member.guild.name} reason {reason}")
        await member.ban(reason=reason)
        await interaction.response.send_message(content=f"done!", ephemeral=True)

async def setup(client:commands.Bot) ->None:
    await client.add_cog(ban(client))
