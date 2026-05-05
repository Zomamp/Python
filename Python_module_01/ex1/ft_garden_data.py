#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    show1 = Plant("Rose", 25, 30)
    show2 = Plant("Sunflower", 80, 45)
    show3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    show1.show()
    show2.show()
    show3.show()
