import discord
import random
from discord.ext import commands


class Fun:
    def __init__(self, client):
        self.client = client

    @commands.command(name = "eightball",
                      description = "Magical 8 Ball")
    async def eightball(self, ctx):
        responses = ["It is certain",
                     "It is decidedly so",
                     "Without a doubt",
                     "Yes - definitely",
                     "You may rely on it",
                     "As I see it, yes",
                     "Most likely",
                     "Outlook good",
                     "Yes",
                     "Signs point to yes",
                     "Reply hazy, try again",
                     "Ask again later",
                     "Better not tell you now",
                     "Cannot predict now",
                     "Concentrate and ask again",
                     "Don't count on it",
                     "My reply is no",
                     "My sources say no",
                     "Outlook not so good",
                     "Very doubtful"]
        response = random.choice(responses) + ", " + ctx.message.author.mention
        await self.client.say(response)


def setup(client):
    client.add_cog(Fun(client))
