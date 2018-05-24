from __future__ import unicode_literals
import discord
import asyncio
import praw
import random
import sys
import pprint
import urllib
import locale
from pybooru import Danbooru
from discord.ext.commands import Bot
from discord.ext import commands

locale.setlocale(locale.LC_ALL,'')
Client = discord.Client()
bot_prefix="/"
client = commands.Bot(command_prefix=bot_prefix)

#Reddit API Pull
pp = pprint.PrettyPrinter(indent=4)
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')
subreddit_list = {'anime_irl':['anime_irl'], 'hatsune':['hatsune'], 'blackpeopletwitter':['blackpeopletwitter'], 'fireemblemheroes':['fireemblemheroes'], 'MEOW_IRL':['MEOW_IRL'], 'peoplefuckingdying':['peoplefuckingdying'], 'animemes':['animemes'], 'animeow_irl':['animeow_irl'], 'smugs':['smugs'], 'cutelittlefangs':['cutelittlefangs'], 'rarekumikos':['rarekumikos'], 'dankruto':['dankruto']}
subreddit_with_caption = {'fireemblemheroes':True, 'peoplefuckingdying':True, 'anime_irl':False, 'hatsune':False, 'blackpeopletwitter':False, 'MEOW_IRL':False, 'animemes':False, 'animeow_irl':False, 'smugs':False, 'cutelittlefangs':False, 'rarekumikos':True, 'dankruto':False}

subscription_type = {'hatsune':'all', 'anime_irl':'day','blackpeopletwitter':'month', 'fireemblemheroes':'day', 'MEOW_IRL':'day', 'peoplefuckingdying':'month', 'animemes':'day', 'animeow_irl':'month', 'smugs':'all', 'cutelittlefangs':'all', 'rarekumikos':'all', 'dankruto':'week'}
print(reddit.user.me())
submission_url="Broken :frowning2:"
result="Broken :frowning2:"

def __init__(self, bot):
 	self.bot = bot

#Returns subreddit shit
def submission_parser(submission, subreddit):
    global submission_url
    global subreddit_with_caption

    print (submission.title)
    print (submission.url)
    submission_title = submission.title

    if subreddit_with_caption[subreddit] == True:

      submission_url = "http://www.reddit.com" + submission.permalink
    else:
      submission_url = submission.url

def subredditScraper(input_call):
  #define global variables
  global subreddit_list
  global subscription_type

  #define local variables
  final_list = []

  sub_list = subreddit_list[input_call] #returns Array type
    
  for sub in sub_list:
    current_subreddit = reddit.subreddit(sub)
    print (current_subreddit.title)

    for sub_post in current_subreddit.top(subscription_type[input_call], limit=200):
      final_list.append(sub_post)

  post_index = random.randint(0, len(final_list) - 1)
  submission_parser(final_list[post_index], input_call)

#Changes Miku bot's Playing status.
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type /help!'))

#Miku replies. Main source of interaction!
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    message.content = message.content.lower() 
    if message.author == client.user:
        return

#Miku says hi!
    if message.content.startswith('/hello'):
        msg = '{0.author.mention} ハーロ！'.format(message)
        await client.send_message(message.channel, msg)

#Miku says hi!
    if message.content.startswith('/hi'):
        msg = '{0.author.mention} ハーロ！'.format(message)
        await client.send_message(message.channel, msg)

#Miku says bye :(
    if message.content.startswith('/bye'):
    	msg = '{0.author.mention} バイバイ :frowning:'.format(message)
    	await client.send_message(message.channel, msg)

#Miku says 39!
    if message.content.startswith('/thanks'):
    	msg = '{0.author.mention} サンキュー！:three::nine:'.format(message)
    	await client.send_message(message.channel, msg)

    if message.content.startswith('/arigatou'):
    	msg = '{0.author.mention} サンキュー！:three::nine:'.format(message)
    	await client.send_message(message.channel, msg)

#Miku's energized!
    if message.content.startswith('/genki'):
    	msg = '元気だよー！'.format(message)
    	await client.send_message(message.channel, msg)

#Miku shitposts!
    if message.content.startswith('/anime_irl'):
    	subredditScraper("anime_irl")
    	msg = submission_url.format(message)
    	await client.send_message(message.channel, msg)

#Miku posts selfies!
    if message.content.startswith('/miku'):
	    subredditScraper("hatsune")
	    msg = submission_url.format(message)
	    await client.send_message(message.channel, msg)

#Miku posts from /r/blackpeopletwitter
    if message.content.startswith('/bptwitter'):
	    subredditScraper("blackpeopletwitter")
	    msg = submission_url.format(message)
	    await client.send_message(message.channel, msg)

#Miku posts from /r/fireemblemheroes
    if message.content.startswith('/feh'):
	    subredditScraper("fireemblemheroes")
	    msg = submission_url.format(message)
	    await client.send_message(message.channel, msg)

#Miku posts from /r/MEOW_IRL
    if message.content.startswith('/meow_irl'):
	    subredditScraper("MEOW_IRL")
	    msg = submission_url.format(message)
	    await client.send_message(message.channel, msg)

#Miku posts from /r/peoplefuckingdying
    if message.content.startswith('/peoplefuckingdying'):
	    subredditScraper("peoplefuckingdying")
	    msg = submission_url.format(message)
	    await client.send_message(message.channel, msg)
#Miku posts from /r/animemes
    if message.content.startswith('/animemes'):
	    subredditScraper("animemes")
	    msg = submission_url.format(message)
	    await client.send_message(message.channel, msg)
        
#Miku posts from /r/animeow_irl
    if message.content.startswith('/animeow_irl'):
        subredditScraper("animeow_irl")
        msg = submission_url.format(message)
        await client.send_message(message.channel, msg)
        
#Miku posts from /r/smugs
    if message.content.startswith('/smugs'):
        subredditScraper("smugs")
        msg = submission_url.format(message)
        await client.send_message(message.channel, msg)
        
#Miku posts from /r/cutelittlefangs
    if message.content.startswith('/fangs'):
        subredditScraper("cutelittlefangs")
        msg = submission_url.format(message)
        await client.send_message(message.channel, msg)
        
#Miku posts from /r/rarekumikos
    if message.content.startswith('/rarekumikos'):
        subredditScraper("rarekumikos")
        msg = submission_url.format(message)
        await client.send_message(message.channel, msg)
		
#Miku posts from /r/dankruto
	if message.content.startswith('/dankruto'):
		subredditScraper("dankruto")
		msg = submission_url.format(message)
		await client.send_message(message.channel, msg)
		
#Miku sends a list of help commands!
    if message.content.startswith('/help'):
	    msg = 'Hello {0.author.mention}! Here is a list of commands that Miku recognizes! ```Markdown\n\n\n# List of Commands # \n\n/hello, /hi - Miku says hi! \n\n/genki - Miku returns her energy levels! \n\n/thanks, /arigatou - Miku says thanks! \n\n/bye - Miku says bye :( \n\n/poke - Miku gets poked. \n\n/hugs - Miku hugs you! \n\n/anime_irl, bptwitter, peoplefuckingdying, meow_irl, animeow_irl, animemes, rarekumikos, feh, smugs, fangs - Miku posts images from the subreddit.```'.format(message)
	    await client.send_message(message.channel, '{0.author.mention} I\'ve sent you a list of commands!'.format(message))
	    await client.send_message(message.author, msg)

#Miku gets poked and replies!
    if message.content.startswith('/poke'):
    	msg = ['やめて！', 'やーやめろー！', '何？', 'もう。。。', 'おい！', 'ん？', 'いや！', 'きゃー！']
    	await client.send_message(message.channel, random.choice(msg))

    if message.content.startswith('/hugs'):
    	msg = 'Miku hugs {0.author.mention}!'.format(message)
    	await client.send_message(message.channel, msg)

    if message.content.startswith('/poll'):
    		msg = await client.send_message(message.channel, 'Reaction poll!!')
    		msg = await client.add_reaction(message, '👍')
    		msg = await client.add_reaction(message, '👎')
    		msg = await client.add_reaction(message, '🤷')

client.run("")
