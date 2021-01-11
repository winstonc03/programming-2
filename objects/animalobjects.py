# animalobjects.py
# practice object-oriented programming
# in the context of animals

class Animal:
    # constructor
    def __init__(self):
        self.name = "Undefined"
        self.legs = 0

    def talk(self):
        if self.name != "Undefined":
            print(f"yooo my name's {self.name}")
        else:
            print("yooo")


# creating an animal object
some_animal = Animal()

# access properties
some_animal.name = "Rex"
some_animal.legs = 2

chad_leg_animal = Animal()
chad_leg_animal.name = "Chad"
chad_leg_animal.legs = 20

print(chad_leg_animal.name)
print(chad_leg_animal.legs)
chad_leg_animal.talk()




