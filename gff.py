import random

# 🎲 Random student names and favorite subjects
students = ["CoderZ", "Bytey", "Loopster", "TechNova", "FuncFox"]
subjects = ["Math", "Science", "History", "Coding", "Art"]

# 🌀 Pick random intro name and subject
name = random.choice(students)
fav_subject = random.choice(subjects)

# 📄 File to modify
file_name = "class_intro.txt"

# ✅ 1. Open file in read mode and print content
try:
    with open(file_name, "r") as f:
        content = f.read()
        print("📖 Current file content:\n", content)
except FileNotFoundError:
    print("⚠️ File not found. Let's create it first.")

# ✅ 2. Open file in write mode and overwrite with random intro
with open(file_name, "w") as f:
    f.write(f"Hello! I'm {name}. Nice to meet you! 🎉\n")

# ✅ 3. Open file in append mode to add favorite subject
with open(file_name, "a") as f:
    f.write(f"My favorite subject is {fav_subject}. 📚\n")

# ✅ 4. File is auto-closed with 'with' blocks
print("\n✅ All steps complete! File updated with random student intro.")
