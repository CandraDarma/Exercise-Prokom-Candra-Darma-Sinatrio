person_1 = {"first_name": "Candra", "last_name": "Darma", "age": 19, "city": "Salatiga"}
person_2 = {"first_name": "Rafa", "last_name": "Pratama", "age": 20, "city": "Yogyakarta"}
person_3 = {"first_name": "Estrelyta", "last_name": "Shayna", "age": 18, "city": "Salatiga"}

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()
