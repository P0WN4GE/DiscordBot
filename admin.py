import discord
from discord.ext import commands


class Admin:
    def __init__(self, client):
        self.client = client

    @commands.command(name="status",
                      description='Change /"Playing/" status')
    async def status(self, newStatus):
        await self.client.change_presence(game = discord.Game(name = newStatus))

    @commands.command(name="load",
                      description="Load a Cog",
                      usage="load [cog]")
    async def load(self, extension):
        try:
            self.client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded, [{}]'.format(extension, error))

    @commands.command(name="unload",
                      description="Unload a Cog",
                      usage="unload [cog]")
    async def unload(self, extension):
        try:
            self.client.unload_extension(extension)
            print('Unloaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be unloaded, [{}]'.format(extension, error))


def setup(client):
    client.add_cog(Admin(client))
