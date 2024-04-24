from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Герой выбрал меч")

class Bow(Weapon):
    def attack(self):
        print("Герой выбрал лук")

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print("Нет оружия")

class Monsters:
    def __init__(self, name):
        self.name = name

#Пример

fighter = Fighter("Воин")
sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
fighter.attack()

monster = Monsters("Гаргулья")
print(f"Герой {fighter.name} сразился с монстром {monster.name}.")
print(f"Монстр {monster.name} побежден!")

fighter.change_weapon(bow)
fighter.attack()
monster = Monsters("Гаргулья")
print(f"Герой {fighter.name} сразился с монстром {monster.name}.")
print(f"Монстр {monster.name} побежден!")