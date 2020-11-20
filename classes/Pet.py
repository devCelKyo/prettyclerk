seuils_xp = [0]
for i in range(40):
    seuils_xp.append(10*i)
    
class Pet:
    def __init__(self, nom, element, stars, stats):
        self.nom = nom
        self.element = element
        self.level = 1
        self.xp = 0
        self.stars = stars
        self.level_max = 5 + self.stars*5
        self.stats = stats

    def give_xp(self, amount):
        self.xp += amount
        self.check_lvl()

    def check_lvl(self):
        for i in range(len(seuils_xp)):
            if self.xp >= seuils_xp[i]:
                self.level = i

    def evolve(self, feed):
        ok = True
        if len(feed) != self.stars:
            ok = False
        for feed_pet in feed:
           if feed_pet.stars != self.stars:
               ok = False
        if self.level != self.level_max:
            ok = False

        if ok:
            self.stars += 1
            self.level = 1
            self.level_max = 5 + self.stars*5

    def __repr__(self):
        pr = "{} (".format(self.nom)
        pr += self.stars*"⭐"
        pr += ") - Lv. {} - {}".format(self.level, self.element)
        return pr
        
