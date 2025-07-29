import string, random

def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.sample(chars, length))
    return password

print("Random Password:", generate_password())
