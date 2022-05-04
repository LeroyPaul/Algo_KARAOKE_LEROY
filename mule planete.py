import random

class Ressource :
    def __init__(self,nom,prix):
        self.__name = nom
        self.__price = prix
        self.__bourse = 0
    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getBourse(self,alea):
        self.__price = self.__price + alea
        return  self.__price

crystite = Ressource("Crystite",48)
smithore = Ressource("Smithore",50)
food = Ressource("Food",10)

energy = Ressource("Energy",10)

tableau=[crystite,smithore,food,energy]
for i in range (4):
    print(tableau[i].getName())

game = True
jour = 0

while game != False :
    jour += 1
    print ("Jour ",jour)
    alea=random.randint(-10,10)
    truc=random.randint(0,3)
    for i in range (4):
        if (truc == i):                                                                                                                                                                                                         
            truc = tableau[i].getName()
            
            if (alea >0):
                print("Vous vendez",alea,truc,"à",tableau[i].getPrice(),"crédits")
                tableau[i].getBourse(alea)
            if (alea <0):
                bidule = (-alea)
                print("Vous achetez",bidule,truc,"à",tableau[i].getPrice(),"crédits")
                tableau[i].getBourse(alea)

