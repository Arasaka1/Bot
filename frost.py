import discord
import asyncio
import requests
import json

client = discord.Client()
user = 'sMlgjAbrTY2EY71A'
key = '9tFQ4K7XnaRvLWh4WESFTYXLxQoF9Cs6'

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='chat with me!'))

@client.event
async def on_message(message):
    if not message.author.bot and (message.server == None or client.user in message.mentions):
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )

print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('Mzg2MzI3MjA1Mjc5NDMyNzA1.DQXVsw.Cv0l0N1zYBZA4-37PLSE6YuTIpw')
