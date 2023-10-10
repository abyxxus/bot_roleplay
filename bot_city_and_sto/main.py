import discord
import config_db
from discord.ext import commands

description = '''bot destinado creacion de ciudades y mas enfocados para el rolplay.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

key =  open("key.txt", "r")

guilds = 0

#evento que revisa accesibilidad al servidor y toma la id
@bot.event
async def on_guild_available(guild):
    global guilds
    guilds = guild.id
    print(f'El servidor {guild.name} está disponible.')

#evento que notifica la coneccion del bot y la id de coneccion 
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-'*100)


#comando para crear ciudad y su canal
@bot.command()
async def t(ctx, message):
    
     # Verifica si el usuario tiene el rol específico
    role = discord.utils.get(ctx.guild.roles, id= [1158593294633279520,1158593352682459298]) # Reemplaza con el nombre del rol

    if role in ctx.author.roles:
        await ctx.send("¡Tienes el rol necesario para ejecutar este comando!")
    else:
        await ctx.send("No tienes el rol necesario para ejecutar este comando.")

bot.run(key.read())