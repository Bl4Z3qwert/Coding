# 🛎️ List to store slam book entries
slam_book = []

# 🎉 Fun random name generator (no real names used!)
import random
nicknames = ["WhizBot", "CoderZ", "ByteSpark", "Loopster", "ScriptNova", "TechieTaco"]

print("🎓 Welcome to the Python Slam Book!")
num_entries = int(input("How many friends do you want to add? "))

for i in range(num_entries):
    print(f"\n📄 Friend #{i + 1} Entry")
    friend_name = random.choice(nicknames)
    fav_color = input(f"{friend_name}, what's your favorite color? ")
    fav_food = input(f"{friend_name}, what's your favorite food? ")