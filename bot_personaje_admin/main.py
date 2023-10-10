import discord
import confi
from discord.ext import commands

#variables
key = open("token.txt", "r") #config lectura de token
guilds = None #id de la guild

#conig  basica bot
description = '''bot destinado a la creacion administrativa de las ciudades y sus derivados para rol play.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

#seccion de eventos que toma el bot
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-'*100)

#seccion de comandos que toma el bot
@bot.group()# inicio comandos para creacion de raza version admnistrativa
async def raza(ctx):
    if ctx.invoked_subcommand is None:
    
        embed = discord.Embed(title="comandos para crear una razas", description="lista de comandos", color = discord.Color.blurple())
        
        embed.add_field(name="1. crear raza", value="```>raza name <nombre de la raza>``` (con este comando se crea la raza)", inline=False)
        embed.add_field(name="2. crear historia", value="```>raza historia <archivo txt> o <texto de la historia>```", inline=False)
        embed.add_field(name="3. crear stats", value="```>raza stats <vida:int> <fuerza:int> <agilidad:int> <inteligencia:int> <fe:int> <persepcion:int> <precision:int> (no es necesario poner los prefijo pero si el orden)```", inline=False)
        embed.add_field(name="4. seleccionar pais de origen", value="```>raza reino <nombre del reino>(este sera limitante nacionalidad para los pj's)```", inline=False)

        
        await ctx.send(embed=embed)

#comando para crear una raza atravez del nombre 
@raza.command()
async def nombre (ctx, message):
    data = confi.raza_name(message)
    
    if data != None:
        embed = discord.Embed(title = "error al crear raza", 
                              description=f"la raza **{message}** ya existe, puede establecer los siguientes datos",
                              color = discord.Color.magenta())
        
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title = "crear raza", 
                              description=f"raza creada bajo el nombre **{message}**",
                              color = discord.Color.magenta())
        await ctx.send(embed = embed)

#comando para crear o actualizar la historia de las razas
@raza.command()
async def historia (ctx, message):
    print(message)
    print(ctx)
    
    data = ctx.message.content.split()
    
    print(data)
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(attachment.filename)
        
        state = confi.raza_history(data[2], attachment)
        
        print(attachment)
    else:
        his = []
        for i in range(len(data)):
            if i > 2:
                his.append(data[i])
        
        his = ' '.join(i for i in his)
        print(his)
        state = confi.raza_history(data[2], his)
    
    if state:
        embed = discord.Embed(title = "creacion o actualizacion de hitoria", description = f"se actualizo la historia de {data[2]}", color = discord.Color.red())
        await ctx.send(embed = embed)
    else:
        await ctx.send(f"primero crear la raza de {data[2]}")

@raza.command()
async def stats(ctx, message):
    data = ctx.message.content.split()
    print(data)
    print(message)
    
    final = []
    
    try:
        for dat in range(3,10,1):
            final.append(data[dat])
        
        state = confi.raza_stats(message, final)
    except Exception:
        embed = discord.Embed(title="ERROR", description="faltaron datos", color = discord.Color.green())
        await ctx.send(embed = embed)
        
    print(final)
    if state:
        embed = discord.Embed(title="creado con exito", description=f"se actualizaron los datos de {message}", color = discord.Color.green())
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="ERROR", description="no exite la raza, porfavor cree la raza antes", color = discord.Color.green())
        await ctx.send(embed = embed)

@raza.command()
async def pais(ctx):
    #comando por construir
    await ctx.send("en construccion")
#fin de los sub-comandos de raza

@bot.group()#inicio comandos para la creacion de clases
async def clases(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="comandos para crear una clase", description="lista de comandos para crear clases", color=discord.Color.blurple())
        
        
        await ctx.send(embed = embed)

@clases.command()
async def nombre(ctx, message):
    data = confi.class_name(message)
    
    if data != None:
        embed = discord.Embed(title = "error al crear la clase", 
                              description=f"la clase **{message}** ya existe, puede establecer los siguientes datos",
                              color = discord.Color.magenta())
        
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title = "crear clase", 
                              description=f"clase creada bajo el nombre **{message}**",
                              color = discord.Color.magenta())
        await ctx.send(embed = embed)

bot.run(key.read())