import random
from dataclasses import dataclass


@dataclass
class BanRoulette:
    Users: list[str]

    def Nemesis(self):
        nemesisList = {}
        random.shuffle(self.Users)
        for nome in self.Users:
            burnList = self.Users.copy()
            burnList.remove(nome)
            Target = random.sample(burnList, 2)
            nemesisList[nome] = {"Nemesi": Target, "Punti": 0, "Selezione": []}
        return nemesisList

    def Vote(self):
        nemesisList = self.Nemesis()

        for e in nemesisList:
            while True:
                V = input("Quali persone ha votato {}? ".format(e))
                Vote = list(V.split(" "))

                if Vote[0] == e and len(Vote) == 1:
                    nemesisList[e]["Selezione"].extend(Vote)
                    nemesisList[e]["Punti"] = 3
                    break
                elif len(Vote) == 3 and all(v != e for v in Vote):
                    nemesisList[e]["Selezione"].extend(Vote)
                    for v in Vote:
                        nemesisList[v]["Punti"] += 1
                    break
                else:
                    print("Voto errato: Inserire o il proprio nome, o tre nomi diversi")

        print(nemesisList)


BR = BanRoulette(["Mirco", "Sam", "Cipri", "Feggio", "Ferra", "Fer", "Dona", "Jack", "Volpe", "Rick"])
BR.Vote()

