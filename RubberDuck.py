# e22mcag0011
# Kunal Nirankari
from Duck import Duck
from fly_no_way import FlyNoWay
from Squeak import Squeak

class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self):
        print("I am a Rubber Duck")
