class Person:
    name = ""
    hp = 100
    mood = 0
    money = 0

    def __init__(self, name, hp=100, mood=100, money=0):
        self.name = name
        self.health = hp
        self.damage = mood
        self.defence = money

    def show_info(self):
        print(self.__str__())

    def __str__(self):
        return f' = {self.name} =\n' \
               f' hp: {self.hp}\n' \
               f' mood: {self.mood}\n' \
               f' money: {self.money}\n' \

    def change_states(self, hp, mood, money):
        self.hp -= hp
        self.mood -= mood
        self.money -= money
        return hp, mood, money