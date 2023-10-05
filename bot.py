import discord
from discord.ext import commands
from ai import get_class
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def alo(ctx):
    await ctx.send(f'buenas, soy {bot.user}, cabro\' certificado')

@bot.command()
async def jiji(ctx, count_heh = 5):
    await ctx.send("xd" * count_heh)

@bot.command()
async def tomapng(ctx):
    await ctx.send(f'juro que como esto sea un meme me cagare en todo')
    attachments = ctx.message.attachments
    for i in range(len(attachments)):
        if i > 0:
            await ctx.send(f'chaval eso son demasiadas pngs')
            return(False)
        else:
            await ctx.send(f'ANALIZANDO IMAGEN. POR FAVOR ESPERE.')
            print(attachments)
            if attachments[0].filename.__contains__(".png"):
                await attachments[0].save("images/usersubmitted/atch.png")
                aimagicks = get_class(modelroute="keras_model.h5", tagroute="labels.txt", imageroute="images/usersubmitted/atch.png")
                if aimagicks == "Class 1":
                    aimagicks = ("ajaja q wen meme xd por favor aiudenme, pq LE VOI A LANZAR 30 BOMBAS")
                else:
                    aimagicks = ("respetos obtenidos")
                await ctx.send(aimagicks)
                return(True)
            else:
                await ctx.send(f'Eso no es un png- BUMMMM VA EL BERGABUS')
                return(False)
    else:
        await ctx.send(f"mmmWOMP")
bot.run("ajaja NO TOKEN 4 U")