class Character:
    name = ""
    hp = 100
    damage = 1
    defence = 0

    def __init__(self, name, hp=100, damage=1, defence=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence

    def show_info(self):
        print(f' = {self.name} =\n'
              f'Health: {self.hp} =\n'
              f'Damage: {self.damage} =\n'
              f'Defence: {self.defence} =\n')
    def take_damage(self, damage):
        self.hp -= damage
        return damage

    def attack(self, target):
        return target.take_damage(self.damage)