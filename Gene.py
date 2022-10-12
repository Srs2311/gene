# testing
import os
import discord
import random
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
class Gene(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1029149757651812352

    async def on_ready(self):
        print("ready")

    async def on_message(self, message):

        guild = message.guild.id
        member = message.author




        strmember = str(member)
        mess = str(message.content)
        mess = mess.lower()
        if message.author == client.user:
            return
        else:
            #let gene know hes a good boy
            if message.content.lower() == "!headpat gene":
                print("headpat " + strmember)
                response = "https://tenor.com/view/patpat-pat-comfort-pat-on-the-head-there-there-gif-10534102"
                await message.channel.send(response)
            # output info i need to know
            elif message.content.lower() == "!debug test":
                response = message.content
                print("debug test " + strmember)
                response = ("Debug:" + strmember)
                await message.channel.send(response)
            elif mess.startswith("!xkcd "):
                xkcdnum = str(message.content).strip("!xkcd ")
                response = "https://xkcd.com/" + xkcdnum + "/"
                print(response + " " + strmember)
                await message.channel.send(response)

            elif mess.startswith("!tf2 "):
                tf2wiki = str(message.content).replace("!tf2 ", "")
                print(tf2wiki)
                tf2wiki = tf2wiki.replace(" " , "_")
                print(tf2wiki)
                response = "https://wiki.teamfortress.com/wiki/" + tf2wiki
                print(response + " " + strmember)
                await message.channel.send(response)

            elif message.content.lower() == "!sesh":
                #Sends a random gif from and pings the sesh role
                print("Sesh" + " " + strmember)
                randnum = random.randint(1,4)

                if randnum == 1:
                    response = "https://tenor.com/view/weed-time-weed-judge-judy-bud-flower-gif-22124013"
                    await message.channel.send(response)
                elif randnum == 2:
                    response = "https://tenor.com/view/t2s-creeping-gif-21232075"
                    await message.channel.send(response)
                elif randnum == 3:
                    response = "https://tenor.com/view/cat-weed-pokemon-high-cartoon-gif-25778108"
                    await message.channel.send(response)
                elif randnum == 4:
                    response = "https://tenor.com/view/weed-walking-leaf-marijuana-cheech-gif-24443001"
                    await message.channel.send(response)
                await message.channel.send("<@&1029203597038194699> its toking time")
            elif message.content.lower() == "!gougar":
                response = "https://i.kym-cdn.com/photos/images/original/002/423/540/730.png"
                print(strmember + " gougar")
                await message.channel.send(response)



    async def on_raw_reaction_add(self, payload):
        # give a role based on a reaction emoji

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        strmember = str(member)
        hehim = 1029244039633043466
        sheher = 1029244075267854356
        theythem = 1029244111397589073
        hethey = 1029244059056881704
        shethey = 1029244095111114794
        anypro = 1029244119396143165
        minecraft = 1029245131708178442
        DnD = 1029245178223005746
        tf2 = 1029245228957306950
        Sesh = 1029245189115609158
        terraria = 1029245156219695185
        fortnite = 1029245144844742686
        Red = 1029246035010256946
        Green = 1029246039498182686
        Blue = 1029246044631994419
        Pink = 1029187050806714408
        Orange = 1029246065016311970
        Kerbal = 1029246107345232032
        Purple = 1029246074407374920
        Pink = 1029246086092705862


        # if payload.message_id != self.target_message_id:
        # return
        if payload.message_id == hehim:
            if payload.emoji.name == "✅":
                print("added " + strmember + " he/him " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="He/Him")
                await payload.member.add_roles(role)
            else:
                return

        elif payload.message_id == sheher:
            if payload.emoji.name == "✅":
                print("added " + strmember + " She/Her " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="She/Her")
                await payload.member.add_roles(role)
            else:
                return
        elif payload.message_id == theythem:
            if payload.emoji.name == "✅":
                print("added " + strmember + " They/Them " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="They/Them")
                await payload.member.add_roles(role)
        elif payload.message_id == hethey:
            if payload.emoji.name == "✅":
                print("added " + strmember + " He/They " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="He/They")
                await payload.member.add_roles(role)
        elif payload.message_id == shethey:
            if payload.emoji.name == "✅":
                print("added " + strmember + " She/They " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="She/They")
                await payload.member.add_roles(role)
            else:
                return
        elif payload.message_id == anypro:
            if payload.emoji.name == "✅":
                print("added " + strmember + " Any pronouns " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Any pronouns")
                await payload.member.add_roles(role)
        elif payload.message_id == minecraft:
            if payload.emoji.name == "💎":
                print("added " + strmember + " minecraft " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Minecraft")
                await payload.member.add_roles(role)
        elif payload.message_id == DnD:
            if payload.emoji.name == "🐉":
                print("added " + strmember + " D&D " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="D&D")
                await payload.member.add_roles(role)
        elif payload.message_id == Red:
            if payload.emoji.name == "🍎":
                print("added " + strmember + " red " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Red")
                await payload.member.add_roles(role)
        elif payload.message_id == Green:
            if payload.emoji.name == "🍏":
                print("added " + strmember + " green " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Green")
                await payload.member.add_roles(role)
        elif payload.message_id == Blue:
            if payload.emoji.name == "🫐":
                print("added " + strmember + " blue " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Blue")
                await payload.member.add_roles(role)
        elif payload.message_id == Purple:
            if payload.emoji.name == "🍆":
                print("added " + strmember + " purple " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Purple")
                await payload.member.add_roles(role)
        elif payload.message_id == Pink:
            if payload.emoji.name == "🍑":
                print("added " + strmember + " pink " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Pink")
                await payload.member.add_roles(role)
        elif payload.message_id == Orange:
            if payload.emoji.name == "🍊":
                print("added " + strmember + " Orange " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Orange")
                await payload.member.add_roles(role)
        elif payload.message_id == Kerbal:
            if payload.emoji.name == "kerbal":
                print("added " + strmember + " Kerbal " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Kerbal")
                await payload.member.add_roles(role)
        elif payload.message_id == Sesh:
            if payload.emoji.name == "high":
                print("added " + strmember + " Sesh " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Toker")
                await payload.member.add_roles(role)
        elif payload.message_id == tf2:
            if payload.emoji.name == "tf2":
                print("added " + strmember + " tf2 " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="tf2")
                await payload.member.add_roles(role)
        elif payload.message_id == terraria:
            if payload.emoji.name == "terraria":
                print("added " + strmember + " terraria " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Terraria")
                await payload.member.add_roles(role)
        elif payload.message_id == fortnite:
            if payload.emoji.name == "jonesy":
                print("added " + strmember + " fortnite squad " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Fortnite Squad")
                await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        # removes a role based on a reaction emoji

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        strmember = str(member)

        hehim = 1029244039633043466
        sheher = 1029244075267854356
        theythem = 1029244111397589073
        hethey = 1029244059056881704
        shethey = 1029244095111114794
        anypro = 1029244119396143165
        minecraft = 1029245131708178442
        DnD = 1029245178223005746
        tf2 = 1029245228957306950
        Sesh = 1029245189115609158
        terraria = 1029245156219695185
        fortnite = 1029245144844742686
        Red = 1029246035010256946
        Green = 1029246039498182686
        Blue = 1029246044631994419
        Pink = 1029187050806714408
        Orange = 1029246065016311970
        Kerbal = 1029246107345232032
        Purple = 1029246074407374920
        Pink = 1029246086092705862

        # if payload.message_id != self.target_message_id:
        # return
        if payload.message_id == hehim:
            if payload.emoji.name == "✅":
                print("removed " + strmember + " he/him " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="He/Him")
                await member.remove_roles(role)
            else:
                return

        elif payload.message_id == sheher:
            if payload.emoji.name == "✅":
                print("removed " + strmember + " She/Her " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="She/Her")
                await member.remove_roles(role)
            else:
                return
        elif payload.message_id == theythem:
            if payload.emoji.name == "✅":
                print("removed " + strmember + " They/Them " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="They/Them")
                await member.remove_roles(role)
        elif payload.message_id == hethey:
            if payload.emoji.name == "✅":
                print("removed " + strmember + " He/They " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="He/They")
                await member.remove_roles(role)
        elif payload.message_id == shethey:
            if payload.emoji.name == "✅":
                print("removed " + strmember + " She/They " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="She/They")
                await member.remove_roles(role)
            else:
                return
        elif payload.message_id == anypro:
            if payload.emoji.name == "✅":
                print("removed " + strmember + " Any pronouns " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Any pronouns")
                await member.remove_roles(role)
        elif payload.message_id == minecraft:
            if payload.emoji.name == "💎":
                print("removed " + strmember + " minecraft " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Minecraft")
                await member.remove_roles(role)
        elif payload.message_id == DnD:
            if payload.emoji.name == "🐉":
                print("removed " + strmember + " D&D " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="D&D")
                await member.remove_roles(role)
        elif payload.message_id == Red:
            if payload.emoji.name == "🍎":
                print("removed " + strmember + " red " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Red")
                await member.remove_roles(role)
        elif payload.message_id == Green:
            if payload.emoji.name == "🍏":
                print("removed " + strmember + " green " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Green")
                await member.remove_roles(role)
        elif payload.message_id == Blue:
            if payload.emoji.name == "🫐":
                print("removed " + strmember + " blue " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Blue")
                await member.remove_roles(role)
        elif payload.message_id == Purple:
            if payload.emoji.name == "🍆":
                print("removed " + strmember + " purple " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Purple")
                await member.remove_roles(role)
        elif payload.message_id == Pink:
            if payload.emoji.name == "🍑":
                print("removed " + strmember + " pink " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Pink")
                await member.remove_roles(role)
        elif payload.message_id == Orange:
            if payload.emoji.name == "🍊":
                print("removed " + strmember + " Orange " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Orange")
                await member.remove_roles(role)
        elif payload.message_id == Sesh:
            if payload.emoji.name == "high":
                print("removed " + strmember + " Group sesh " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Toker")
                await member.remove_roles(role)
        elif payload.message_id == tf2:
            if payload.emoji.name == "tf2":
                print("removed " + strmember + " tf2 " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="tf2")
                await member.remove_roles(role)
        elif payload.message_id == terraria:
            if payload.emoji.name == "terraria":
                print("removed " + strmember + " terraria " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Terraria")
                await member.remove_roles(role)
        elif payload.message_id == fortnite:
            if payload.emoji.name == "jonesy":
                print("removed " + strmember + " fortnite squad " + payload.emoji.name)
                role = discord.utils.get(guild.roles, name="Fortnite Squad")
                await member.remove_roles(role)
    # async def on_message(message):
    #   if message.author == client.user:
    #      return
    # if message.content == "ping":
    #    await message.channel.send("pong")


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = Gene(intents=intents)
client.run(TOKEN)
