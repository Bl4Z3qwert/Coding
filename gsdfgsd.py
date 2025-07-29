# ✅ Step 1: Open file and print full content
with open("sample.txt", "r") as file:
    content = file.read()
    print("📄 Full file content:\n", content)

# ✅ Step 2: Print first 10 characters
with open("sample.txt", "r") as file:
    first_ten = file.read(10)
    print("\n🔢 First 10 characters:\n", first_ten)

# ✅ Step 3: Print first line only
with open("sample.txt", "r") as file:
    first_line = file.readline
    