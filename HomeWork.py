from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon_name(weapon)}.")

    def weapon_name(self, weapon):
        if isinstance(weapon, Sword):
            return "меч"
        elif isinstance(weapon, Bow):
            return "лук"
        else:
            return "неизвестное оружие"

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Оружие не выбрано"

class Monster:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return f"{self.name} атакует"

if __name__ == "__main__":
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    sword = Sword()
    bow = Bow()

    fighter.changeWeapon(sword)
    print(fighter.attack())
    print("Монстр побежден!\n")
