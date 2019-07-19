class Animal:
    def speak(self):
        raise NotImplementedError("Subclass need to implemented this method")


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Fish(Animal):
    pass  # error
