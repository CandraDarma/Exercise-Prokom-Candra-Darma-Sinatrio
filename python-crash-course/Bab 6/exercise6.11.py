cities = {
    "jakarta": {
        "country": "Indonesia",
        "population": "10 juta",
        "fact": "ibu kota Indonesia",
    },
    "tokyo": {
        "country": "Japan",
        "population": "14 juta",
        "fact": "kota terpadat di dunia",
    },
    "paris": {
        "country": "France",
        "population": "2 juta",
        "fact": "ada Menara Eiffel",
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")
