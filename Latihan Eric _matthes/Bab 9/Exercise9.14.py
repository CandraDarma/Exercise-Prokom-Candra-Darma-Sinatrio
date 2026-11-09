from random import sample

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]


winning_ticket = sample(lottery_pool, 4)

print("Tiket yang cocok dengan 4 angka/huruf berikut memenangkan hadiah:")
print(winning_ticket)