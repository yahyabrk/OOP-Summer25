# Creating dictionaries for five animals
lion = {
    "name": "Lion",
    "group": "Mammals",
    "number_of_legs": 4,
    "skills": ["roaring", "hunting", "running fast"]
}

falcon = {
    "name": "Falcon",
    "group": "Birds",
    "number_of_legs": 2,
    "skills": ["flying", "hunting", "sharp vision"]
}

dolphin = {
    "name": "Dolphin",
    "group": "Mammals",
    "number_of_legs": 0,
    "skills": ["swimming", "jumping", "communication"]
}

toad = {
    "name": "Toad",
    "group": "Amphibians",
    "number_of_legs": 4,
    "skills": ["jumping", "swimming", "camouflage"]
}

crocodile = {
    "name": "Crocodile",
    "group": "Reptiles",
    "number_of_legs": 4,
    "skills": ["swimming", "hunting", "strong bite"]
}

# Storing all animals in a list
animals = [lion, falcon, dolphin, toad, crocodile]

# Printing each animal's information
for animal in animals:
    print(animal)
