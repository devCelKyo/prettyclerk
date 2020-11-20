import pickle
import os
seuils_xp = [0, 0, 10, 50, 100, 200, 500, 1000, 2500, 4000, 6000]
os.chdir("./data")
data_joueurs = "joueurs"
class Joueur(object):
    
    ''' Représente un joueur (humain) du jeu'''
    def save(self):
        fch = open(data_joueurs, "rb")
        mdp = pickle.Unpickler(fch)
        try:
            dic = mdp.load()
            dic[self.nom] = self
            fch.close()
        except:
            fch = open(data_joueurs, "wb")
            mp = pickle.Pickler(fch)
            dic = dict()
            dic[self.nom] = self
            mp.dump(dic)
            fch.close()
            
        fch = open(data_joueurs, "wb")
        mp = pickle.Pickler(fch)
        mp.dump(dic)
        fch.close()

    def save_dic(dic):
        fch = open(data_joueurs, "wb")
        mp = pickle.Pickler(fch)
        mp.dump(dic)
        fch.close()
        
    def __init__(self, nom, user_id):
        self.nom = nom
        self.id = user_id
        self.level = 1
        self.xp = 0
        self.money = 0
        self.inventaire = []
        self.equipement = {"Collier" : None, "Baguette" : None}
        self.pets = []
        self.save()
        
    def check_lvl(self):
        for i in range(len(seuils_xp)):
            if self.xp >= seuils_xp[i]:
                self.level = i
        self.save()
        
    def give_xp(self, amount):
        self.xp += amount
        self.check_lvl()

    def give_money(self, amount):
        self.money += amount
        self.save()

    def give_item(self, item, amount=1):
        for i in range(amount):
            self.inventaire.append(item)
        self.save()

    def give_pet(self, pet):
        self.pets.append(pet)
        self.save()

    def find_item(self, item):
        for i in range(len(self.inventaire)):
            if self.inventaire[i].nom == item.nom:
                return i

    def has_item(self, item, qte=1):
        s_inv = self.show_inv()
        for s_item in s_inv:
            if (s_item[0].nom == item.nom) and (s_item[1] >= qte):
                return True
        return False
    
    def sell_item(self, item, qte=1):
        if self.has_item(item, qte):
            for k in range(qte):
                self.inventaire.pop(self.find_item(item))
            self.give_money(item.s_prix*qte)
            
    def get_player(nom):
        fch = open(data_joueurs, "rb")
        mdp = pickle.Unpickler(fch)
        dic = mdp.load()
        fch.close()
        try:
            return dic[nom]
        except:
            print("Ce joueur n'existe pas.")

    def get_inv(self):
        return self.inventaire

    def get_pets(self):
        return self.pets

    def count_items(item, inv):
        count = 0
        for s_item in inv:
            if s_item.nom == item.nom:
                count += 1
        return count

    def show_inv(self):
        s_inv = set()
        for s_item in self.inventaire:
            s_inv.add((s_item, Joueur.count_items(s_item, self.inventaire)))
        return s_inv
  
    def flush_inv(self):
        self.inventaire = []
        self.save()

    def player_exists(nom):
        try:
            dic = Joueur.get_players()
            a = dic[nom]
            return True
        except:
            return False

    def get_players():
        fch = open(data_joueurs, "rb")
        mdp = pickle.Unpickler(fch)
        dic = mdp.load()
        fch.close()
        return dic

    def delete_player(obj=None, nom=None):
        '''Attention!!!!'''
        dic = Joueur.get_players()
        try:
            dic.pop(nom)
            Joueur.save_dic(dic)
        except:
            print("Ce joueur n'existe pas.")
    
    def reset(self):
        ''' Attention!!!'''
        self.__init__(self.nom, self.id)

    def flush_players():
        fch = open(data_joueurs, "wb")
        mp = pickle.Pickler(fch)
        mp.dump({})
        fch.close()
    
    def __repr__(self):
        return "Pseudo : {} | Niveau : {} | XP : {} | Argent : {}".format(self.nom, self.level,
                                                            self.xp, self.money)

    
