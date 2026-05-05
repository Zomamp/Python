#!/usr/bin/env python3

class Plant:
    def __init__(self, name, grow, age):
        self.name = name
        self.grow = grow
        self.age = age

    def ft_garden_data(self):
        print(f"{self.name}: {self.grow}cm, {self.age} days old")

    def loop(self):
        growth = 0.0
        for i in range(1, 8):
            print(f"=== Days {i} ===")
            self.grow = round(self.grow + 0.8, 1)
            self.age += 1
            growth += 0.8
            self.ft_garden_data()
        print(f"Growth this week: {growth}")

    def show(self):
        self.loop()


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    see = Plant("Rose", 25.0, 30)
    see.ft_garden_data()
    see.show()
