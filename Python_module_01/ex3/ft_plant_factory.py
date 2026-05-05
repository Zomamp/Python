#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25.6, 132)
    p2 = Plant("Dak", 26.0, 365)
    p3 = Plant("Cactus", 28.1, 90)
    p4 = Plant("Sunflower", 10.4, 45)
    p5 = Plant("Fern", 25.8, 120)
    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()
