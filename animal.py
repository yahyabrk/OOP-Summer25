class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        return f"Name: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"



lion = Animal("Lion", "Mammals", 4, ["roaring", "hunting", "running fast"])
elephant = Animal("Elephant", "Mammals", 4, ["memory", "trumpeting", "swimming"])
eagle = Animal("Eagle", "Birds", 2, ["flying", "sharp vision", "hunting"])
octopus = Animal("Octopus", "Molluscs", 8, ["camouflage", "problem solving", "squeezing through tight spaces"])
shark = Animal("Shark", "Fish", 0, ["swimming fast", "sharp teeth", "excellent sense of smell"])


animals = [lion, elephant, eagle, octopus, shark]
for animal in animals:
    print(animal)
