class Account:
    def __init__(self, name, balance):
        self.__name = name        # Private attribute
        self.__balance = balance  # Private attribute

    def __str__(self):
        return f"Account Holder: {self.__name}, Balance: ${self.__balance}"

    def deposit(self, amount):
        self.__balance += amount
        print(f"${amount} deposited. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance!")

# Example usage
acc = Account("Boubouneh", 500)
print(acc)
acc.deposit(100)
acc.withdraw(200)
