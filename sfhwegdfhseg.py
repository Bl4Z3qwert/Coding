# 🎯 Create a class with a method to greet a user
class Greeter:
    def __init__(self, nickname):
        self.nickname = nickname

    def say_hello(self):
        print(f"👋 Hello, {self.nickname}! Welcome to your Python class.")

# 📥 Input from user
user_nick = input("Enter your nickname: ")
greet_me = Greeter(user_nick)

# 🚀 Call the method
greet_me.say_hello()
