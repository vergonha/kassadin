import discord


class Embeds:

  @staticmethod
  async def embed_days(nick: str, region: str, days: str) -> discord.Embed:
    url_image = 'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'

    embed = discord.Embed(
      description=
      f"Summoner Name: **{nick}**\n**{nick}** is available in **{days}** days!",
      color=0xed377d,
    )

    embed.set_author(
      name=f"Summoner Name: {nick} | Region: {region.upper()}",
      icon_url=
      'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'
    )
    embed.add_field(
      name='-=' * 25,
      value=
      f'🌠   If the nick is in an inactive account, there is no way to get it.\n'
    )
    embed.set_thumbnail(url=url_image)

    return embed

  @staticmethod
  async def embed_available(nick: str, region: str) -> discord.Embed:
    url_image = 'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'

    embed = discord.Embed(
      description=f"Summoner Name: **{nick}**\n**{nick}** is available!",
      color=0x5cfa77,
    )

    embed.set_author(
      name=f"Summoner Name: {nick} | Region: {region.upper()}",
      icon_url=
      'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'
    )
    embed.add_field(
      name='-=' * 25,
      value=f'🌠   Get him before someone else gets it first...\n')
    embed.set_thumbnail(url=url_image)

    return embed

  @staticmethod
  async def embed_probably(nick, region):
    url_image = 'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'

    embed = discord.Embed(
      description=
      f"Summoner Name: **{nick}**\n**{nick}** is probably available!",
      color=0xf2e141,
    )

    embed.set_author(
      name=f"Summoner Name: {nick} | Region: {region.upper()}",
      icon_url=
      'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'
    )
    embed.add_field(
      name='-=' * 25,
      value=
      f'🌠   It may or may not be possible to get it, 50/50\n🌠   If the nick is in a banned account or in an inactive account for a long time, it will not be possible to get it\n'
    )
    embed.set_thumbnail(url=url_image)

    return embed

