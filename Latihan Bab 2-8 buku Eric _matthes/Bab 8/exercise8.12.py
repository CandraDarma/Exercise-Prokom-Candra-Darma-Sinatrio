def make_sandwich(*items):
    print("Making a sandwich with:")
    for item in items:
        print(f"- {item}")


make_sandwich("ham")
make_sandwich("ham", "cheese")
make_sandwich("ham", "cheese", "lettuce", "tomato")