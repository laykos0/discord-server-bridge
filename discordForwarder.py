# Copyright (C) 2020 laykos0 <laykos0@protonmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; version 3 of the License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import discord

# Insert bot token here:
token = ""
client = discord.Client()


async def forward(server_name, message, author, destination):
    for guild in client.guilds:
        if str(guild) != str(server_name):
            for channel in guild.channels:
                if channel.name in destination:
                    embed = discord.Embed()
                    embed.set_author(name=author, icon_url=author.avatar_url)
                    embed.add_field(name="Server:", value=str(server_name), inline=False)
                    embed.add_field(name="Message:", value=message, inline=False)
                    await channel.send(content=None, embed=embed)


@client.event
async def on_message(message):
    # Insert channels from which the bot should forward messages here:
    channels = [""]
    # Define the destination channels here:
    destination = [""]
    # Insert your own bot tag here:
    bot_tag = ""

    if str(message.channel) in channels and str(message.author) != bot_tag:
        await forward(message.guild.name, message.content, message.author, destination)


client.run(token)
