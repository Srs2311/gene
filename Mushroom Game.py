#imports
import os
import discord
import random
import pyodbc
import mysql.connector
from dotenv import load_dotenv

#load token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

#delcare intents (discord perms)
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5RA4pHpnm343C@$xjiv0zVdvy$Jg3PBSz^I",
    database="sys"
                              )
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM playersnew")
myresult = mycursor.fetchall()






class Gene(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1029149757651812352

    async def on_ready(self):
        print("ready")

    async def on_message(self, message):
        #get server and author information and save to a string
        guild = message.guild.id
        member = message.author
        strmember = str(member)
        usrid = message.author.id
        print(str(usrid) + " " + str(message.content))

        mess = str(message.content)
        mess = mess.lower()

        #print(mess)


        mycursor = mydb.cursor()
        mycursor.execute("Select id, score FROM playersnew WHERE id = \"" + str(usrid) + "\"")
        myresult = mycursor.fetchall()
        result = str(myresult)
        #print(myresult)
        #print(result)
        #checks to see if user is already in the database
        if message.author == client.user:
            return
        elif result == "[]":
            sql = "INSERT INTO playersnew (id, score, click, passive) VALUES (%s, %s, %s, %s)"
            val = (usrid, 0, 1, 0)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
        #adds a number to their score based on click value in db
        else:
            #print("test successful")
            #mycursor.execute("Select id, score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
            #userinfo = mycursor.fetchall
            #print(userinfo)

            #pulls score and click value to pass down

            #isolates click value
            mycursor.execute("Select score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
            clickinfo = mycursor.fetchall()
            clickinfo = clickinfo[0]
            index = int(clickinfo[1])
            #isolates score value
            mycursor.execute("Select score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
            scoreinfo = mycursor.fetchall()
            scoreinfo = scoreinfo[0]
            scoreupdate = scoreinfo [0] + index
            print(index)
            print(scoreupdate)
            scorestr = str(scoreupdate)

            #updates users score value according to click value
            mycursor.execute('''UPDATE playersnew SET SCORE = ''' + scorestr + ''' WHERE id = ''' + str(usrid))
            mydb.commit()

            #pulls updated score value
            mycursor.execute("Select score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
            scoreinfo = mycursor.fetchall()
            scoreinfo = scoreinfo[0]
            scoreinfo = scoreinfo [0]
            scorestr = str(scoreinfo)

            print("Your score is now " + scorestr)

            #scoreboard command
            if (message.content) == "!scoreboard":

                mycursor.execute("Select id, score FROM playersnew ORDER BY score")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                    response = x
                    await message.channel.send(response)
            #score command
            elif (message.content) == "!score":
                mycursor.execute("Select id, score FROM playersnew WHERE id = \"" + str(usrid) + "\"")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                    response = x
                    await message.channel.send(response)

            #shop and buy commands
            elif (message.content) == "!shop":
                shopmenu = "Shop menu: \n 1. Mycelium - 10 Shrooms - + 1 Shroom on message \n 2. Uncle Ben's Rice - 20 Shrooms - +2 shrooms on message"
                await message.channel.send(shopmenu)
            elif mess.startswith("!buy"):
                #await message.channel.send("Buy menu coming soon")

                mycursor.execute("Select id, score FROM playersnew WHERE id = \"" + str(usrid) + "\"")
                scoreinfo = mycursor.fetchall()
                scoreinfo = scoreinfo[0]
                scoreinfo = scoreinfo[1]

                itemid = mess.strip("!buy ")
                print(itemid)
                mycursor.execute("Select itemid, cost FROM items WHERE itemid = \"" + str(itemid) + "\"")
                costinfo = mycursor.fetchall()
                costinfo = costinfo[0]
                costinfo = costinfo[1]
                print("score = " + str(scoreinfo))
                print("cost  = " + str(costinfo))
                #makes sure user can afford item
                if(scoreinfo > costinfo):

                    scoreinfo = scoreinfo - costinfo
                    # updates users score value according to click value
                    mycursor.execute('''UPDATE playersnew SET SCORE = ''' + str(scoreinfo) + ''' WHERE id = ''' + str(usrid))

                    await message.channel.send("Purchase completed")
                    print("You spent " + str(costinfo) + " you now have " + str(scoreinfo))
                    mydb.commit()

                    # pulls updated score value
                    mycursor.execute("Select score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
                    scoreinfo = mycursor.fetchall()
                    scoreinfo = scoreinfo[0]
                    scoreinfo = scoreinfo[0]
                    scorestr = str(scoreinfo)

                    #gets click value of the item
                    mycursor.execute("Select clickup, passiveup FROM items WHERE itemid = \"" + str(itemid) + "\"")
                    clickinfo = mycursor.fetchall()
                    clickinfo = clickinfo[0]
                    clickinfo = clickinfo[0]
                    print("The click value of this item is " + str(clickinfo))

                    mycursor.execute("Select score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
                    usrclickinfo = mycursor.fetchall()
                    usrclickinfo = usrclickinfo[0]
                    usrclickinfo = usrclickinfo[1]
                    clickinfo = clickinfo + usrclickinfo
                    print("Your click value is " + str(usrclickinfo))
                    mycursor.execute('''UPDATE playersnew SET CLICK = ''' + str(clickinfo) + ''' WHERE id = ''' + str(usrid))
                    mydb.commit()

                    #pulls updated user click info
                    mycursor.execute("Select score, click FROM playersnew WHERE id = \"" + str(usrid) + "\"")
                    usrclickinfonew = mycursor.fetchall()
                    usrclickinfonew = usrclickinfonew[0]
                    usrclickinfonew = usrclickinfonew[1]
                    print("Your new click value is " + str(usrclickinfonew))
                else:
                    await message.channel.send("too expensive")

client = Gene(intents=intents)
client.run(TOKEN)