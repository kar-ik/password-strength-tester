def dictionary_attack(password, dictionary_file='dictionary.txt'):
    with open(dictionary_file, 'r') as file:
        for line in file:
            if line.strip() == password:
                return password
    return None

if __name__ == "__main__":
    password = input("Enter the password to test: ")
    result = dictionary_attack(password)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
