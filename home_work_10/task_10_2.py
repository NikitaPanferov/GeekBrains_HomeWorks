from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parm):
        self.parm = parm

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return self.parm / 6.5 + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return self.parm * 2 + 0.3


class Cloth:
    clothes = []

    def add_coat(self, parm):
        self.clothes.append(Coat(parm))

    def add_costume(self, parm):
        self.clothes.append(Costume(parm))

    @property
    def full_consumption(self):
        fc = 0
        for i in self.clothes:
            fc += i.consumption

        return fc


cl = Cloth()

cl.add_coat(6.5)
cl.add_costume(4)
print(cl.full_consumption)