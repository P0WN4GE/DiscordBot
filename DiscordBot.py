import discord
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN = "NTcwMjEzMDA0MDg4NDQyOTAw.XL769g.KMJul2iuSAWplhPH5qkYrNRUOHw"
client = commands.Bot(command_prefix='.')
extensions = ['fun', 'admin']
status = ["Msg1", "Msg2", "Msg3"]


'''async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game = discord.Game(name = current_status))
        await asyncio.sleep(5)'''  # Creating a background process, make sure to uncomment the loop at the bottom


@client.event   # Sends Terminal Message when loaded and sets status to .help
async def on_ready():
    await client.change_presence(game = discord.Game(name='.help'))
    print('Bot Online')


@client.command()  # Message Clear Command
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(channel, limit = int(amount)):
        messages.append(message)
    await message.delete(messages)


@client.command(name = "ping") # Ping, need to add timestamp
async def ping():
    await client.send("Pong! :ping_pong:")


@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description',
        color = discord.Colour.blue()
    )

    embed.set_footer(text = 'This is a footer.')
    embed.set_image(url = 'https://media.wired.com/photos/5b5777a34f14ad6ea775fb54/master/pass/zuck-962130580.jpg')
    embed.set_thumbnail(url = "https://media.wired.com/photos/5b5777a34f14ad6ea775fb54/master/pass/zuck-962130580.jpg")
    embed.set_author(name = 'Author Name',
                     icon_url = ctx.message.author.avatar_url)
    embed.add_field(name = ".ping", value = "Field Value", inline = False)
    embed.add_field(name = ".ping", value = "Field Value", inline = True)
    embed.add_field(name = ".ping", value = "Field Value", inline = True)

    await client.send(embed=embed)


@client.command()  # Logs out bot
async def logout():
    await client.send("Logging out :wave:")
    await client.logout()

if __name__ == '__main__': # Load Cogs
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded, [{}]'.format(extension, error))

# client.loop.create_task(change_status())
client.run(TOKEN)
