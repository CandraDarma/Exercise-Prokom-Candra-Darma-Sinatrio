rivers = {"nile": "egypt", "amazon": "brazil", "bengawan solo": "indonesia"}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()
for river in rivers:
    print(river.title())

print()
for country in rivers.values():
    print(country.title())