import os
import discord
from dotenv import load_dotenv
load_dotenv()
CHANNEL = os.getenv("CHANNEL")
TOKEN = os.getenv("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL))
        await channel.send('Hello World')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
print(TOKEN)
client.run(TOKEN)