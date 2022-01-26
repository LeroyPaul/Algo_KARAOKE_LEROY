# Exercice A

class Player:
    def __init__(self,nom):
        self.__name = nom
        self.__listeScore = [0,0,0,0,0]
        self.__moyenne = 0
        self.__total = 0
    def getName(self):
        return self.__name
    def afficherScore(self):
        return self.__listeScore
    def moyenneScore(self):
        total = 0
        for i in range (5):
            total += self.__listeScore[i]
        self.__moyenne = total / 5
        return self.__moyenne
    def ajouterScore(self,numeroChanson,score):
        if score >= 50 and score <= 100 :
            if self.__listeScore[numeroChanson] < score :
                self.__listeScore[numeroChanson] = score
                return self.__listeScore
            else:
                print("votre score doit être plus élevé que le score déjà enregistré pour pouvoir être ajouté")
        else :
            print("votre score doit être entre 50 et 100 pour pouvoir être ajouté")
    def totalScore(self):
        total = 0
        for i in range (5):
            total += self.__listeScore[i]
        self.__total = total
        return self.__total
    def meilleurScore(self):
        meilleur = 0
        for i in range (5):
            if meilleur < self.__listeScore[i]:
                meilleur = self.__listeScore[i]
        return meilleur
    def pireScore(self):
        pire = 0
        pire += 100
        for i in range (5):
            if pire > self.__listeScore[i]:
                pire = self.__listeScore[i]
        return pire


        

#Test implémentation d'objets de class

roger = Player("Roger")

print(roger.getName())
print(roger.afficherScore())
roger.ajouterScore(0,50)
roger.ajouterScore(1,72)
roger.ajouterScore(2,88)
roger.ajouterScore(3,52)
roger.ajouterScore(4,18)
roger.ajouterScore(4,97)
print(roger.afficherScore())
print(roger.moyenneScore())
print(roger.totalScore())
print(roger.meilleurScore())
print(roger.pireScore())
roger.ajouterScore(0,63)
roger.ajouterScore(1,71)
roger.ajouterScore(2,8)
roger.ajouterScore(3,93)
roger.ajouterScore(4,77)
print(roger.afficherScore())

fiona = Player("Fiona")

print(fiona.getName())
print(fiona.afficherScore())
fiona.ajouterScore(0,100)
fiona.ajouterScore(1,54)
fiona.ajouterScore(2,63)
fiona.ajouterScore(3,77)
fiona.ajouterScore(4,99)
print(fiona.afficherScore())
print(fiona.moyenneScore())
print(fiona.totalScore())
print(fiona.meilleurScore())
print(fiona.pireScore())


# Exercice B

class Karaoké:
    def __init__(self,nom,nombreChanson):
        self.__name = nom
        self.__nombreSong = nombreChanson
        self.__nombrePlayer = 1


    def getName(self):
        return self.__name
    def getnombreSong(self):
        return self.__nombreSong
    def getnombrePlayer(self):
        return self.__nombrePlayer