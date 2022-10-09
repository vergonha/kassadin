import discord
from discord.commands import slash_command
from discord.ext import commands
from discord import Option

from embeds import Embeds

import requests
import re


class Check(commands.Cog):

  def __init__(self, bot: discord.Bot):
    self.bot = bot
    self.regions = [
      'BR', 'NA', 'OCE', 'LAS', 'LAN', 'EUNE', 'EUW', 'KR', 'JP', 'RU', 'TR'
    ]
    self.headers = {
      "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

  async def days_left(self, url: str) -> str:
    r = requests.get(url, headers=self.headers).text
    count_down = re.search("available in([^.]*)days", r)
    days = int(count_down.group(1))
    return str(days)

  async def available(self, url: str) -> str:
    try:
      r = requests.get(url, headers=self.headers).text
      if 'is available!</h4>' in r or 'is available!</h2>' in r:
        return "available"
      elif 'is probably available!</h4>' in r:
        return "probably"
      else:
        return await self.days_left(url)
    except Exception as e:
      return "error"

  @slash_command(name="check",
                 description="Check League of Legends nickname availability!",
                 guild_ids=[788333040584753232])
  async def check(self, ctx: discord.ApplicationContext,
                  nickname: Option(str, "Desired nickname", required=True),
                  region: Option(str,
                                 "Nickname region",
                                 choices=[
                                   "BR", "NA", "OCE", "LAS", "LAN", "EUNE",
                                   "EUW", "KR", "JP", "RU", "TR"
                                 ],
                                 required=True),
                  ephemeral: Option(bool,
                                    "Ephemeral message",
                                    default=False,
                                    required=False)):
    url = f'https://lols.gg/en/name/checker/{region}/' + nickname
    result = await self.available(url)
    if result == "available":
      return await ctx.respond(embed = await Embeds.embed_available(nickname, region), ephemeral=ephemeral)
    elif result == "probably":
      return await ctx.respond(embed = await Embeds.embed_probably(nickname, region), ephemeral=ephemeral)
    elif result == "error":
      return await ctx.respond("? XD", ephemeral = True)
    else:
        return await ctx.respond(embed = await Embeds.embed_days(nickname, region, result), ephemeral=ephemeral)

def setup(bot: commands.Bot):
  bot.add_cog(Check(bot))
