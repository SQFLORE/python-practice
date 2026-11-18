class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.depth = depth

    def speak(self):
        print(f'{self.name} молчит...')

    def birthday(self):
        self.age += 1
        print('Плюх!')

f = Fish('Немо', 1, 'banana')
f.speak()
f.birthday()
print(f.name, f.age, f.depth)