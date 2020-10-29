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
