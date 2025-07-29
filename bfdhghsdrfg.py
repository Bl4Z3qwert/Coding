# 📦 Pre-defined dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 🖊️ Ask user for a key
key = int(input("Enter a key (1–6): "))

# 📌 Return the corresponding value
if key in d:
    print(f"🎯 The value for key {key} is: {d[key]}")
else:
    print("⚠️ That key isn’t in the dictionary.")
