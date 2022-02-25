import discord
import os
import requests
import json
from keep_alive import keep_alive
def get_quote():
  response=requests.get("https://zenquotes.io/api/random");
  json_data=json.loads(response.text);
  quote=json_data[0]['q']+" -"+ json_data[0]['a']
  return (quote)
client= discord.Client()
@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author== client.user:
      return
    if message.content.startswith('$inspire'):
      quote=get_quote()
      await message.channel.send(quote)

keep_alive()
client.run(os.environ['TOKEN'])

