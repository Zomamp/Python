#!/usr/bin/env python3

class Plant_security:

    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def creation(self):
        print(
           f"Plant created: {self.name}:"
           f"{self.__height}cm, {self.__age} days old"
         )

    def update(self, height=None, age=None):
        if height is not None:
            if height > 0:
                self.__height = height
                print(f"Height updated: {self.__height}cm")
            else:
                print(f"{self.name}: Error, height can't be negative")
                print("Height update rejected")
        if age is not None:
            if age > 0:
                self.__age = age
                print(f"Age updated: {self.__age} days")
            else:
                print(f"{self.name}: Error, age can't be negative")
                print("Age update rejected")

    def show(self):
        print(
            f"Current state: {self.name}:{self.__height}cm,"
            f"{self.__age} days old"
             )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    up = Plant_security("Rose", 15.2, 30)
    up.creation()
    up.update(height=20, age=5)
    up.show()
