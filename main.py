import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def smd(ctx):
    await ctx.send("gawk gawk ahhh")

@bot.command()
async def fir(ctx, name):
    await ctx.send(f"filed a fir againt {name} for calling me a 20 rupe ki")


bot.run(TOKEN)


