

# 67. Inheritance + super()
class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

c = Cat("Tom", "White")
print(c.name, c.color)


# 68. Custom Length
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["A", "B", "C"])
print(len(t))
