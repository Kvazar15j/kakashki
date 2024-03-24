from ehjr_2.charp1 import Character
from berserk import Berserk

p1 = Character('Pudge', damage=45, health=670)
p1.show_info()

p2 = Berserk('Tidehunter', damage=31, health=714)
print(p2)
while p1.is_alive() and p2.is_alive():
      p1_damage = p1.attack(p2)
      print(f'{p1.name} атакував {p2.name} '
            f'і наніс {p1_damage} шкоди.')
      p2_damage = p2.attack(p1)
      print(f'{p2.name} атакував {p1.name} '
            f'і наніс {p2_damage} шкоди.')

      print(p1, p2, sep='\n')