from random import randint


class Die:
    

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
       
        print(randint(1, self.sides), end=" ")


for sides in (6, 10, 20):
    die = Die(sides)
    print(f"\nDadu {sides} sisi, dilempar 10 kali:")
    for roll_number in range(10):
        die.roll_die()
    print()