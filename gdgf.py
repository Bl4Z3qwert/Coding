# 🚀 Take input from user
base = int(input("Enter the base number: "))
n = int(input("Enter the number of terms: "))

print(f"\n🔢 Power series of {base} up to {n} terms:")

# 🔁 Loop to print power series
for i in range(1, n + 1):
    result = base ** i
    print(f"{base}^{i} = {result}")
