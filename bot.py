
import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Ready!')

@client.event
async def on_member_join(member):
	print('%s has joined the server!' % member)

@client.event
async def on_member_remove(member):
	print('%s has left the server :(' % member)

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command(aliases = ['8ball', 'test'])
async def _8ball(ctx, *, question):
	responses = ["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."]
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 5):
	await ctx.channel.purge(limit = amount )

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
	print(reason)
	await member.kick(reason = reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
	print(reason)
	await member.ban(reason = reason)


@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	print(banned_users)
	member_name, member_number = member.split('#')


client.run('NzU1NTg2NjkzMjgwNTYzMjMx.X2Fc8Q.Zq3irNCjXvZUkoKc73uwyzgRIUU')
