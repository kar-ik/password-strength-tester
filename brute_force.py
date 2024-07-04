import itertools
import string

def brute_force(password):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, 9):  # You can adjust the length for testing
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if guess == password:
                return guess
    return None

if __name__ == "__main__":
    password = input("Enter the password to test: ")
    result = brute_force(password)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
