# 🔍 Function to check for Disarium Number
def is_disarium(num):
    total = 0
    for index, digit in enumerate(str(num)):
        total += int(digit) ** (index + 1)
    return total == num

# 🧮 Input from user
user_number = int(input("Enter a number to check if it's Disarium: "))

# 🚦 Check and print result
if is_disarium(user_number):
    print(f"🎉 {user_number} is a Disarium number!")
else:
    print(f"❌ {user_number} is not a Disarium number.")
