import random
import string

def gen_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Enter password length: "))
print("Generated Password:", gen_password(length))
