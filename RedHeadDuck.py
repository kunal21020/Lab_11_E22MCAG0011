# e22mcag0011
# Kunal Nirankari
from Duck import Duck
from fly_with_wings import FlyWithWings
from MuteQuack import MuteQuack

class RedHeadDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), MuteQuack())

    def display(self):
        print("I am a Red Head Duck")
