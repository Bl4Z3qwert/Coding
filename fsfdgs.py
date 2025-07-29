# 🖊️ Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# 🔎 Check for greatest number
if num1 > num2:
    if num1 > num3:
        print("🏆 num1 is the greatest among three.")
    else:
        print("🏆 num3 is the greatest among three.")
else:
    if num2 > num3:
        print("🏆 num2 is the greatest among three.")
    else:
        print("🏆 num3 is the greatest among three.")
