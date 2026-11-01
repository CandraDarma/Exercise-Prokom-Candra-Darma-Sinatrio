pets = [
    {"animal": "cat", "owner": "Andi"},
    {"animal": "dog", "owner": "Budi"},
    {"animal": "bird", "owner": "Citra"},
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()
