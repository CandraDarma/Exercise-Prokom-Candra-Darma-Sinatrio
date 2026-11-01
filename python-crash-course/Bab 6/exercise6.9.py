favorite_places = {
    "andi": ["Bali", "Yogyakarta"],
    "budi": ["Bandung"],
    "citra": ["Lombok", "Malang", "Bromo"],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"  - {place}")
