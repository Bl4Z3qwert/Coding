import os

# 📌 File name
file_name = "sample_doc.txt"
new_file_name = "My_File.txt"

# ✅ 1. Open file using with() and write your brief introduction
with open(file_name, "w") as f:
    f.write("Hi! I'm Boubouneh, a creative coder exploring Python file magic. ✨\n")

# ✅ 2. Split contents into words and print all the words
with open(file_name, "r") as f:
    content = f.read()
    words = content.split()
    print("🗂️ Words in file:", words)

# ✅ 3. Check if 'My_File.txt' exists
if not os.path.exists(new_file_name):
    print("🔎 'My_File.txt' not found. Creating it...")
    with open(new_file_name, "w") as nf:
        nf.write("Hello again! This is a new file created by Boubouneh. 🌟\n")