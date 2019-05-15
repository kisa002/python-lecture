import random

class Dice(object):
    face = 0

    def Roll(self):
        self.face = random.randint(1, 6)
        print("Dice: " + str(self.face))

dice = Dice()

for _ in range(5):
    dice.Roll()