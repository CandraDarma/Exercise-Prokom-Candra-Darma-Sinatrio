from random import sample

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

my_ticket = [3, 7, "b", "e"]

attempts = 0
while True:
    attempts += 1
    drawn = sample(lottery_pool, 4)
   
    if set(drawn) == set(my_ticket):
        break

print(f"Tiket saya: {my_ticket}")
print(f"Perlu {attempts} kali undian sampai tiket saya menang.")