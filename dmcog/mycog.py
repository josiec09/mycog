from redbot.core import commands

class Mycog(commands.Cog):
    """My custom cog"""

    @client.event
	async def mycom(message):
    if message.content.startswith("#whatever you want it to be")
        await client.send_message(message.author, "#The message")