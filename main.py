import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('your bot is now online!')
    await client.change_presence(status=discord.Status.idle)

client.run("token_here")
