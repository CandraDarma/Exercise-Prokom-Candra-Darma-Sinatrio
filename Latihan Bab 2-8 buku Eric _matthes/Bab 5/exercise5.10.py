current_users = ["Andi", "Budi", "Citra", "Dewi", "Eko"]
new_users = ["andi", "Fajar", "CITRA", "Gita", "Hana"]

current_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_lower:
        print(f"{new_user}: please enter a new username.")
    else:
        print(f"{new_user}: username is available.")
