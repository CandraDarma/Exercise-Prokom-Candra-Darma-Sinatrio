print("kopi" == "kopi")           # True
print("kopi" != "kopi")           # False

# lower()
print("KOPI".lower() == "kopi")   # True
print("KOPI".lower() == "KOPI")   # False

# angka
print(5 == 5, 5 != 5)             # True False
print(3 > 2, 3 > 5)               # True False
print(3 < 5, 3 < 2)               # True False
print(5 >= 5, 4 >= 5)             # True False
print(5 <= 5, 6 <= 5)             # True False

# and / or
print(3 > 2 and 5 > 4)            # True
print(3 > 2 and 5 < 4)            # False
print(3 < 2 or 5 > 4)             # True
print(3 < 2 or 5 < 4)             # False

# item dalam list
buah = ["apel", "jeruk", "mangga"]
print("apel" in buah)             # True
print("pisang" in buah)           # False
