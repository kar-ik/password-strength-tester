import itertools
import string

def brute_force_attack(target_password):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for password_length in range(1, 9):  # You can adjust the range for longer passwords
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                return attempts, guess

if __name__ == "__main__":
    target = "password123"
    attempts, found_password = brute_force_attack(target)
    print(f"Password found: {found_password} in {attempts} attempts")
