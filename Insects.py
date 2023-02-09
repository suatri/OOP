# Create a class for an insect object. It should have 2 attributes –
# wings and legs. For now, the insect object has 2 wings and 4 legs.
# It should also have 1 method – to determine the length of flight.
# Length of flight should be a method that randomly assigns a number between 1 and 10 miles.
# Create a python program that will create an instance of the insect class and print out how
# many miles the insect can fly.
import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def length_of_flight(self):
        self.flight = random.randint(0, 10)

    def land(self):
        return self.flight
