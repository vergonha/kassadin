import os
import discord

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"You're null and void ~ {bot.user}")
  
for filename in os.listdir('commands'):
  if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')  

token = os.environ['token_discord']
my_secret = os.environ['token_discord']
bot.run(os.environ['token_discord'])
