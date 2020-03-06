# define our Animal Class.

# sudo
# Looks / Characteristics of every animal
    # name, age, colour heart, brain

# Behaviours / Methods of every animal
    # eat, sleep, reproduce, potty, make_sound


class Animal:
    # define_behaviours and characteristics

    # define the characteristics of EVERY animal
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.heart = True
        self.brain = 'in works'

    # defining the method .eat(), .sleep(), .reproduce()
    def eat(self):
        return 'Nom nom nom'

    def sleep(self):
        return 'zzzZZzzz'

    def reproduce(self):
        return "I going to need some privacy here..."

    def potty(self):
        return "HUMM!! AHHH! SPLOSH!!"

    def make_sound(self):
        return 'woof'

# To call methods we need an object of this class
# To create an instance of class animal

ringo = Animal('ringo', 20, 'blue') # creates instance of class animal and assigns to variable ringo
# checking and print the instance
print(type(ringo))

# calling methods on instance of Animals
print(ringo.sleep())
print(ringo.eat())
print(ringo.potty())

 # check the attribute of an instance

print(ringo.name)
print(ringo.age)
print(ringo.color)

 # second animal
mini = Animal('stacy', 30, 'yellow')

print(mini.name)