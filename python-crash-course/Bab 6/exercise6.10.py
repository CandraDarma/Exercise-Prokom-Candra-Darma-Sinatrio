favorite_numbers = {
    "andi": [7, 3],
    "budi": [3],
    "citra": [9, 1, 4],
    "dewi": [1, 8],
    "eko": [5, 2],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")
