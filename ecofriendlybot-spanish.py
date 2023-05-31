import discord, random, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def consejo(ctx):
    consejos = [
        'Recuerda apagar las luces cuando no las necesites para ahorrar energía.',
        'Utiliza transporte público o comparte coche para reducir la contaminación del aire.',
        'Evita el uso de plásticos de un solo uso y opta por alternativas reutilizables.',
        'Planta árboles en tu comunidad para ayudar a combatir el cambio climático.',
        'Reduce tu consumo de agua cerrando el grifo mientras te cepillas los dientes o lavas los platos.',
        'Recicla tus residuos correctamente para minimizar el impacto ambiental.',
        'Compra productos locales y de temporada para reducir la huella de carbono del transporte.',
        'Ahorra papel imprimiendo solo cuando sea necesario y utiliza papel reciclado.',
        'Participa en actividades de limpieza comunitaria para mantener el medio ambiente limpio.',
        'Informa a otras personas sobre la importancia de cuidar el medio ambiente y cómo pueden contribuir.'
    ]
    consejo_aleatorio = random.choice(consejos)
    await ctx.send(consejo_aleatorio)

@bot.command()
async def articulos(ctx):
    sitios_web = [
        'https://www.ecologiaverde.com/consejos-para-el-buen-uso-de-la-basura-1590.html',
        'https://www.nationalgeographic.es/medio-ambiente/2020/09/como-reducir-residuos-domesticos',
        'https://www.ecoembes.com/es/blog/buenas-practicas-para-tirar-la-basura',
        'https://www.consumer.es/medio-ambiente/los-10-mandamientos-del-reciclaje-en-casa.html',
        'https://www.sostenibilidad.com/que-es-sostenibilidad/gestion-residuos/buenas-practicas-uso-los-contenedores/'
    ]
    sitio_web_aleatorio = random.choice(sitios_web)
    await ctx.send(sitio_web_aleatorio)


bot.run("not giving you my token. what am I, stupid?")
