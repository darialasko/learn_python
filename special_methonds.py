from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        # sprawdzam czy other jest instancją klasy Human
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        # multyplying human
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Can't multiply"


j = Human("Jenny", "Jones", 43)
k = Human("Brad", "Lorent", 45)

print(j + k)
triplets = j * 3
triplets[1].first = "Jessica"
print(triplets)
# normalnie bez importowania copy w kazdym by nam zamienilo imie, po importowaniu copy zmieni nam tylko w drugim
triplets = (k + j)*3
print(triplets)
