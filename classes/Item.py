class Item:
    def __init__(self, nom, b_prix=0, s_prix=0, item_type=None, usable=None, equip=None):
        self.nom = nom
        self.b_prix = b_prix
        self.s_prix = s_prix
        self.item_type = item_type
        self.usable = usable
        self.equip = equip

    def __repr__(self):
        return self.nom

class Stuff(Item):
    def __init__(self, nom, b_prix=0, s_prix=0, item_type=None, stats=None, lv_min=1):
        Item.__init__(self, nom, b_prix, s_prix, item_type, usable=False, equip=True)
        self.stats = stats
        self.lv_min = lv_min

class Food(Item):
    def __init__(self, nom, b_prix=0, s_prix=0, item_type=None, faim=0):
        Item.__init__(self, nom, b_prix, s_prix, item_type, usable=True, equip=False)
        self.faim = faim

class Scroll(Item):
    def __init__(self, nom, b_prix=0, s_prix=0, item_type=None, tier=0, element=None):
        Item.__init__(self, nom, b_prix, s_prix, item_type, usable=True, equip=False)
        self.tier = tier
        self.element = element
