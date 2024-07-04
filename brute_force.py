import itertools
import string
from tqdm import tqdm

def brute_force(password, max_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    total_combinations = sum(len(characters) ** i for i in range(1, max_length + 1))
    with tqdm(total=total_combinations, desc="Processing") as pbar:
        for length in range(1, max_length + 1):
            for guess in itertools.product(characters, repeat=length):
                guess = ''.join(guess)
                if guess == password:
                    return guess
                pbar.update(1)
    return None

if __name__ == "__main__":
    password = input("Enter the password to test: ")
    max_length = len(password) + 2  # Adjust the range as needed
    result = brute_force(password, max_length)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
