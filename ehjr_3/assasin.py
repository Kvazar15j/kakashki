from ehjr_2.charp1 import Character
import random

a = random.randint(1, 10)

class Assasin(Character):

    def __init__(self, name, health=100, damage=1, defence=0):
        super().__init__(name, health, damage, defence)
        self.max_health = health

    def attack(self, target):
        if a > 8:
            ultra_damage = (100)
        return target.take_damage(
        round(self.damage+ultra_damage)
    )



