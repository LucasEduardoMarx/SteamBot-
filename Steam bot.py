import discord
from discord.ext import commands
import requests

intents=discord.Intents.default()
intents.message_content=True

bot= commands.Bot(command_prefix="!",intents=intents)

@bot.event

async def on_ready():
    print(f"O Bot{bot.user} acabou de entrar!")

@bot.command()
async def preco(ctx, appid: int):
    url= f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=br&l=pt"

    response=requests.get(url)
    data=response.json()

    jogo=data[str(appid)]

    if not jogo["success"]:
        await ctx.send("Jogo não encontrado!")
        return

    info=jogo["data"]

    nome=info["name"]

    if "price_overview" in info:
        preco=info ["price_overview"]["final_formatted"]
        desconto=info ["price_overview"]["discount_percent"]
    else:
        preco="Gratuito"
        desconto= 0
    embed=discord.Embed(
        title=f"🎮 {nome}",
        color=0x00ff00
    )
    if "header_image" in info:
        embed.set_image(url=info["header_image"])
    embed.add_field(name="Preço",value=preco, inline=False)
    embed.add_field(name="Desconto",value=f"{desconto}%", inline=False)
    embed.add_field(
    name="Loja",
    value=f"https://store.steampowered.com/app/{appid}",
    inline=False
)
    await ctx.send(embed=embed)
@bot.command()
async def ajuda(ctx):
    await ctx.send(
        "📌 Comandos disponíveis:\n"
        "!preco <appid> - Ver preço de um jogo da Steam\n"
        "Exemplo: !preco 730\n"
        "Ou procurar pelo nome do jogo!\n"
        "Exemplo: !elden ring"
    )
@bot.command()
async def jogo(ctx, *, nome):
    await ctx.send(f"🔎 Buscando \"{nome}\" na Steam...")

    url = f"https://steamcommunity.com/actions/SearchApps/{nome}"
    response = requests.get(url)
    resultados = response.json()

    if not resultados:
        await ctx.send("❌ Jogo não encontrado!")
        return

    # pegar até 5 resultados
    lista = resultados[:5]

    mensagem = "🎮 Resultados encontrados:\n\n"

    for i, jogo in enumerate(lista, start=1):
        mensagem += f"{i}. {jogo['name']} (ID: {jogo['appid']})\n"

    mensagem += "\nUse !preco <ID> para ver detalhes"

    await ctx.send(mensagem)
bot.run("Seu Token aqui")

