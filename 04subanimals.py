class Animal:
    def __init__(self, energy=50):
        self.energy = energy
        print('I am coming to life!')
    def eat(self, amount):
        self.energy += amount
    def move(self):
        self.energy -= 10
        print('I am running!')
    def get_status(self):
        print('My energy level is', self.energy)
        if (self.energy < 0):
            print('I\'m staving!')
        elif (self.energy > 0 and self.energy < 50):
            print('I\'m getting hungry!')
        elif (self.energy <= 100 and self.energy >= 50):
            print('I\'m happily full.')
        else:
            print('I\'m feeling stuffed!')
    def say_hi(self):
        print('Meep!')

class Penguin(Animal):
    def __init__(self, energy=100):
        self.energy = energy
        print('I am a penguin!')
    def move(self):
        self.energy -= 5
        print('I am sliding!')

class Eagle(Animal):
    def __init__(self, energy=20):
        self.energy = energy
        print('I am an eagle!')
    def move(self):
        if (self.energy < 0):
            print('I am too tired to fly...')
        else:
            self.energy -= 20
            print('I am flying to the sea!')
    def say_hi(self):
        print('Shrieeeeek!')

animal = Animal()
animal.get_status()
animal.eat(60)
animal.get_status()
animal.move()
animal.get_status()
animal.say_hi()
print()

penguin = Penguin()
penguin.eat(5)
penguin.get_status()
penguin.move()
penguin.get_status()
penguin.say_hi()
print()

eagle = Eagle()
eagle.say_hi()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
print()
