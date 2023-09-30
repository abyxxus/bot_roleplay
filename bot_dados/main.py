import discord
from discord.ext import commands
import random

description = '''bot destinado a los dados enfocados para el rolplay.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-'*100)
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        try:
            rolls, limit = map(str, dice.split('d'))
            rolls =int(rolls)
            num1, num2 = map(int, limit.split('+'))
            limit = num1 + num2
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
    
    result = '\n'.join(str(random.randint(1, limit)) for r in range(rolls))
    
    print(f"No.dados: {rolls}")
    print(f"No.caras: {limit}")
    print(f"resultados: {result}")
    print('-'*20)
    
    await ctx.send(result)

bot.run('MTE1Nzc4ODI3MTQ1MjEwNjg5NA.Gql0JO.WX-RoZXOXEg5NKA-KjRDMEUmdxHbLA4AqrFSQs')