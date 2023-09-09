import json
import discord
from discord.ext import commands

message = None

# elements role ids
water_id = 1148728509926211614
earth_id = 1148728239578157116
fire_id  = 1148728291893727282
air_id   = 1148728453605097532

# water_id = 1148933891701346374
# earth_id = 1148941443247902810
# fire_id  = 1148933929672380517
# air_id   = 1148941410062573578

intents = discord.Intents.all()
intents.guilds = True
intents.messages = True
intents.reactions = True
# intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print('client ready')

# sends a start message at this location, there can only be one
@client.command(name="spawnTurtle")
async def create_turtle(ctx):
    global message

    embed=discord.Embed(title="Wähle dein Element", 
                        description=
                        """💦 Wasser 
                         🔥 Feuer
                        🪨 Erde
                         💨 Luft 
                         
                         Das Element, das du wählst, wird dir helfen, dich auf dem Server zurechtzufinden!
                         @everyone
                         """, 
                        color=0x91FF00)

    embed.set_thumbnail(url="https://media.tenor.com/aojw6qKlgnkAAAAC/atla-avatar.gif")

    message = await ctx.channel.send(embed=embed)
    
    await message.add_reaction('💦')
    await message.add_reaction('🪨')
    await message.add_reaction('🔥')
    await message.add_reaction('💨')

    await ctx.message.delete()

# applies role afer reaction
@client.event
async def on_reaction_add(reaction, user):
    global message
    global water_id
    global earth_id
    global fire_id
    global air_id

    if str(user) == "Lion Turtle#3106":
        return
    if message == None:
        return
    if reaction.message != message:
        return
    if reaction.emoji == "💦":
      role = discord.utils.get(reaction.message.guild.roles, id=water_id)
      await user.add_roles(role)
      
      role = discord.utils.get(reaction.message.guild.roles, id=earth_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=fire_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=air_id)
      await user.remove_roles(role)

      other_elements = reaction.message.reactions

      for other in other_elements:
          if other.emoji == "💦":
              continue
          await message.remove_reaction(other.emoji, user)

    if reaction.emoji == "🪨":
      role = discord.utils.get(reaction.message.guild.roles, id=earth_id)
      await user.add_roles(role)
      
      role = discord.utils.get(reaction.message.guild.roles, id=water_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=fire_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=air_id)
      await user.remove_roles(role)

      other_elements = reaction.message.reactions

      for other in other_elements:
        if other.emoji == "🪨":
            continue
        await message.remove_reaction(other.emoji, user)

    if reaction.emoji == "🔥":
      role = discord.utils.get(reaction.message.guild.roles, id=fire_id)
      await user.add_roles(role)
      
      role = discord.utils.get(reaction.message.guild.roles, id=water_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=earth_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=air_id)
      await user.remove_roles(role)

      other_elements = reaction.message.reactions

      for other in other_elements:
        if other.emoji == "🔥":
            continue
        await message.remove_reaction(other.emoji, user)

    if reaction.emoji == "💨":
      role = discord.utils.get(reaction.message.guild.roles, id=air_id)
      await user.add_roles(role)
      
      role = discord.utils.get(reaction.message.guild.roles, id=water_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=earth_id)
      await user.remove_roles(role)
      role = discord.utils.get(reaction.message.guild.roles, id=fire_id)
      await user.remove_roles(role)

      other_elements = reaction.message.reactions

      for other in other_elements:
        if other.emoji == "💨":
            continue
        await message.remove_reaction(other.emoji, user)

# remove role :: Not Functioning
# @client.event
# async def on_reaction_remove(reaction, user):
#     print("hi")
   
#     global water_id
#     global earth_id
#     global fire_id
#     global air_id

#     role = discord.utils.get(reaction.message.guild.roles, id=air_id)
#     await user.remove_roles(role)
#     role = discord.utils.get(reaction.message.guild.roles, id=water_id)
#     await user.remove_roles(role)
#     role = discord.utils.get(reaction.message.guild.roles, id=earth_id)
#     await user.remove_roles(role)
#     role = discord.utils.get(reaction.message.guild.roles, id=fire_id)
#     await user.remove_roles(role)


# handle discord token
config_file = open("config.json", "r").read()
config = json.loads(config_file)
token = config["token"]
client.run(token)
