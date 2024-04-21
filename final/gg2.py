from gg import Person
import random

human = Person(name="Илюша", hp=100, mood=100, money=0)
human.change_states(
        money=random.randint(50, 100),
        mood=random.randint(20, 10),
        hp=random.randint(10, 5)
    )

human2 = Person(name="Игорь", hp=100, mood=70, money=20)
human3 = Person(name="Дядя Миша", hp=70, mood=100, money=50)
print(human)
