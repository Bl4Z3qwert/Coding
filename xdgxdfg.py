# 📘 Slam book entries stored as a list of dictionaries
slam_book = []

# 🎯 Number of friends to record
num_friends = int(input("How many friends do you want to add to your slam book? "))

for i in range(num_friends):
    print(f"\n📄 Enter details for Friend #{i + 1}")
    name = input("Name: ")
    fav_color = input("Favorite color: ")
    fav_food = input("Favorite food: ")
    hobby = input("Hobby: ")
    
    entry = {
        "Name": name,
        "Favorite Color": fav_color,
        "Favorite Food": fav_food,
        "Hobby": hobby
    }
    slam_book.append(entry)

# ✅ Show slam book contents
print("\n📘 Your Slam Book:")
for i, friend in enumerate(slam_book, 1):
    print(f"\n--- Friend {i} ---")
    for key, value in friend.items():
        print(f"{key}: {value}")
