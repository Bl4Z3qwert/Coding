def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "⚠️ Cannot divide by zero"
    else:
        return "❌ Invalid operator"

while True:
    print("\n🧮 Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Operator (+, -, *, /): ")
        result = calculate(num1, num2, op)
        print("🔹 Result:", result)
    except ValueError:
        print("❗ Please enter valid numbers.")

    cont = input("Another calculation? (yes/no): ").lower()
    if cont != "yes":
        print("👋 Calculator exited.")
        break
