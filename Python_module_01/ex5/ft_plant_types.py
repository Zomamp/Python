#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def base(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomy = False

    def bloom(self):
        print("[asking the rose to bloom]")
        self.bloomy = True
        self.base()
        print(f"Color: {self.color}")
        print("Rose is blooming beautifully\n")

    def show(self):
        print("== Flower")
        self.base()
        print(f"Color: {self.color}")
        print("Rose has not bloomed yet")
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk = trunk
        self.produce = False

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        self.produce = True
        print(
            f"Tree Oak now produces a shade of"
            f"{self.height}cm long and {self.trunk}cm wide.\n"
            )

    def show(self):
        print("== Tree")
        self.base()
        print(f"Trunk diameter: {self.trunk}cm")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest, nutritional):
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutritional = nutritional

    def ask_to_grow(self):
        print("[make tomato grow and age for 20 days]")
        self.height += 42
        self.age += 20
        self.base()
        self.nutritional += 20
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self.nutritional}")

    def show(self):
        print("== Vegetable")
        self.base()
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self.nutritional}")
        self.ask_to_grow()


if __name__ == "__main__":
    p1 = Flower("Rose", 15, 12, "red")
    p1.show()
    p2 = Tree("Oak", 200.0, 365, 5.0)
    p2.show()
    p3 = Vegetable("Tomato", 5.0, 10, "April", 0)
    p3.show()
