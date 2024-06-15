def dictionary_attack(target_password, dictionary_file='dictionary.txt'):
    attempts = 0

    with open(dictionary_file, 'r') as f:
        for line in f:
            attempts += 1
            word = line.strip()
            if word == target_password:
                return attempts, word

    return attempts, None

if __name__ == "__main__":
    target = "password123"
    attempts, found_password = dictionary_attack(target)
    print(f"Password found: {found_password} in {attempts} attempts" if found_password else "Password not found")
