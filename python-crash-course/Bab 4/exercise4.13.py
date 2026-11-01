foods = ("nasi", "ayam", "tempe", "sayur", "es teh")
for food in foods:
    print(food)

# foods[0] = "mie"   -> TypeError, tuple tidak bisa diubah

foods = ("nasi", "bebek", "tempe", "sayur", "jus jeruk")
print("\nMenu baru:")
for food in foods:
    print(food)
