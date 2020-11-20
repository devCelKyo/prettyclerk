import discord
import pickle
from discord.ext import commands
from classes.Joueur import Joueur
from classes.Item import Item, Stuff, Food, Scroll


TOKEN = 'Nzc4Mjg1ODM5NTA3NjUyNjE5.X7PxKw.-JdSmyjHFZl9ZBsVQiFAaa88S4Y'
bot = commands.Bot(command_prefix="!")

@bot.command()
async def ping(ctx):
    print("cece")
    await ctx.send("pong")

@bot.command()
async def play(ctx):
    message = ctx.message
    chan = message.channel
    if not Joueur.player_exists(str(message.author)):
        try:
            j = Joueur(str(message.author), 1)
            await chan.send("Votre personnage a bien été crée, à l'aventure!!")
        except:
            await chan.send("Oups... problème...")
    else:
        j = Joueur.get_player(str(message.author))
        await chan.send("Votre personnage existe déjà, il s'agit de : {}"
                            .format(j))

@bot.command()
async def inventory(ctx):
    message = ctx.message
    chan = message.channel
    if not Joueur.player_exists(str(message.author)):
        await chan.send("Vous n'avez pas de personnage, tapez !play pour jouer !")
    else:
        j = Joueur.get_player(str(message.author))
        s_inv = j.show_inv()
        if len(s_inv) != 0:
            msg = "Vous avez : \n"
            i = 1
            for item in s_inv:
                msg += "{} - {} x{} ({} SN/u) \n".format(i, item[0], item[1], item[0].s_prix)
                i += 1
            await chan.send(msg)
            return s_inv
        else:
            await chan.send("Votre inventaire est vide :(")

@bot.command()
async def sell(ctx):
    message = ctx.message
    chan = message.channel
    if not Joueur.player_exists(str(message.author)):
        await chan.send("Vous n'avez pas de personnage, tapez !play pour jouer !")
        return False

    s_inv = await inventory(ctx)
    await ctx.send("Que voulez-vous vendre ? (Répondez avec le numéro de l'item correspondant ci-dessus)")

    def check(m):
        try:
            nbr = int(m.content)
            if nbr > len(s_inv):
                return False
            return True
        except:
            return False
    try:
        msg = await bot.wait_for("message", check=check, timeout=60.0)
    except:
        await ctx.send("Temps écoulé ou réponse invalide. Vente annulée")
        return False

    choix = int(msg.content) - 1
    j = Joueur.get_player(str(message.author))
    i=0
    it=None
    for item in s_inv:
        it=item
        if i==choix:
            break
        i +=1
        
    def check(m):
        try:
            nbr = int(m.content)
            if nbr > it[1]:
                return False
            return True
        except:
            return False

    await ctx.send("Combien voulez vendre de '{}' (Qte disponible : {}) ?".format(it[0], it[1]))
    
    try:
        qte = await bot.wait_for("message", check=check, timeout=60.0)
    except:
        await ctx.send("Temps écoulé ou réponse invalide. Vente annulée")
        return False
    j.sell_item(it[0], int(qte.content))
    await ctx.send("Vous avez bien vendu {} x{} pour {} SN !".format(it[0], qte.content,
                                                                   it[0].s_prix*int(qte.content)))
    
@bot.command()
async def money(ctx):
    message = ctx.message
    chan = message.channel
    if not Joueur.player_exists(str(message.author)):
        await chan.send("Vous n'avez pas de personnage, tapez !play pour jouer !")
    else:
        j = Joueur.get_player(str(message.author))
        await chan.send("Vous avez : {} SN".format(j.money))

@bot.command()
async def pets(ctx):
    message = ctx.message
    chan = message.channel
    if not Joueur.player_exists(str(message.author)):
        await chan.send("Vous n'avez pas de personnage, tapez !play pour jouer !")
    else:
        j = Joueur.get_player(str(message.author))
        pets_list = j.get_pets()
        msg = "Liste de vos pets : \n"
        if len(pets_list) != 0:
            for pet in pets_list:
                msg += "- {} \n".format(pet)
            await chan.send(msg)
        else:
            await chan.send("Vous n'avez pas de pet !")

@bot.command()
async def bae(ctx):
    await ctx.send("i love you so damn much wtf")
    
@bot.command()
async def cece(ctx):
    await ctx.send("77 rue d'amiens VILLERS-BRETONNEUX")
   
@bot.event
async def on_ready():
    print('cc')

bot.run(TOKEN)
