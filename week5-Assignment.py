--- Question1 ---

class Superhero:
    def __init__(self, name, alias, power, origin):
        self._name = name              # encapsulated (private-ish) attributes
        self._alias = alias
        self._power = power
        self._origin = origin
    
    def introduce(self):
        return f"I am {self._alias}, also known as {self._name} from {self._origin}."
    
    def use_power(self):
        return f"{self._alias} uses their power: {self._power}!"

    def get_identity(self):  # Encapsulation via getter
        return self._name

    def set_identity(self, new_name):  # Encapsulation via setter
        self._name = new_name

class IceHero(Superhero):
    def __init__(self, name, alias, origin, freeze_level):
        super().__init__(name, alias, "Cryokinesis", origin)
        self.freeze_level = freeze_level  # unique attribute

    def use_power(self):
        # Polymorphism in action: overrides base method
        return f"{self._alias} freezes everything in sight with intensity {self.freeze_level}!"

class FireHero(Superhero):
    def __init__(self, name, alias, origin, flame_color):
        super().__init__(name, alias, "Pyrokinesis", origin)
        self.flame_color = flame_color

    def use_power(self):
        return f"{self._alias} blasts {self.flame_color} flames into the sky!"

frost = IceHero("Elsa Arctik", "Frostbite", "Glacier City", freeze_level=9000)
blaze = FireHero("Blaze Ignis", "Inferno", "Volcano Valley", flame_color="blue")

print(frost.introduce())
print(frost.use_power())

print(blaze.introduce())
print(blaze.use_power())





--- Question2 ---

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚢")

class Dog:
    def move(self):
        print("Running 🐕")

class Bird:
    def move(self):
        print("Flying 🐦")

# List of different objects
things_that_move = [Car(), Plane(), Boat(), Dog(), Bird()]

# Polymorphic behavior
for thing in things_that_move:
    thing.move()
