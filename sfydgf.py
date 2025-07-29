def calculate_due(total, paid):
    due = total - paid
    return due

total = float(input("Enter total amount: "))
paid = float(input("Enter amount paid: "))
print("Amount due:", calculate_due(total, paid))
