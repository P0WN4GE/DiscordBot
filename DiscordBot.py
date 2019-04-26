import discord
from discord.ext import commands
import asyncio
from itertools import cycle

tokenFile = open("token", "r")
token = tokenFile.read(59)
TOKEN = token  # Don't forget to add token
client = commands.Bot(command_prefix='.')
extensions = ['fun', 'admin']
status = ["Msg1", "Msg2", "Msg3"]

# To Do:
# Fix serverinfo members section
'''async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game = discord.Game(name = current_status))
        await asyncio.sleep(5)'''  # Creating a background process, make sure to uncomment the loop at the bottom


@client.event   # Sends Terminal Message when loaded and sets status to .help
async def on_ready():
    game = discord.Game(".help")
    await client.change_presence(status = discord.Status.idle, activity = game)
    print('Bot Online')


@client.command()  # Message Clear Command
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(channel, limit = int(amount)):
        messages.append(message)
    await message.delete(messages)


@client.command(name = "ping")  # Ping, need to add timestamp
async def ping(ctx):
    await ctx.channel.send("Pong! :ping_pong:")


@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text = 'This is a footer.')
    embed.set_image(url = 'https://media.wired.com/photos/5b5777a34f14ad6ea775fb54/master/pass/zuck-962130580.jpg')
    embed.set_thumbnail(url = "https://media.wired.com/photos/5b5777a34f14ad6ea775fb54/master/pass/zuck-962130580.jpg")
    embed.set_author(name = 'Author Name',
                     icon_url = ctx.message.author.avatar_url)
    embed.add_field(name = ".ping", value = "Field Value", inline = False)
    embed.add_field(name = ".ping", value = "Field Value", inline = True)
    embed.add_field(name = ".ping", value = "Field Value", inline = True)

    await ctx.channel.send(embed=embed)


@client.command()  # Logs out bot
async def logout(ctx):
    await ctx.channel.send("Logging out :wave:")
    await client.logout()


@client.command()
async def serverinfo(ctx):
    server = ctx.message.guild
    embed = discord.Embed(
        colour = discord.Color.blue()
        )

    embed.set_thumbnail(url = server.icon_url)
    embed.set_author(name = server.name,
                     icon_url = server.icon_url)
    embed.add_field(name = "Owner", value = server.owner.display_name, inline = True)
    embed.add_field(name = "Region", value = str(server.region), inline = True)
    embed.add_field(name = "Voice Channels", value = str(len(server.voice_channels)), inline = True)
    embed.add_field(name = "Text Channels", value = str(len(server.text_channels)), inline = True)
    members = server.members
    for member in members:
        if member.bot:
            members.remove(member)
    embed.add_field(name = "People", value = str(len(members)), inline = False)

    await ctx.channel.send(embed=embed)


if __name__ == '__main__': # Load Cogs
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded, [{}]'.format(extension, error))

# client.loop.create_task(change_status())
client.run(TOKEN)
