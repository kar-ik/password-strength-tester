import os

def dictionary_attack(password, dictionary_file):
    if not os.path.exists(dictionary_file):
        print(f"Dictionary file {dictionary_file} not found.")
        return None

    with open(dictionary_file, 'r') as file:
        for line in file:
            if line.strip() == password:
                return password
    return None

if __name__ == "__main__":
    # List of available dictionary files
    dictionaries = ["indianpass.txt", "uspass.txt", "10000000.txt"]

    # Verify the existence of dictionary files
    available_dictionaries = [d for d in dictionaries if os.path.exists(d)]
    if not available_dictionaries:
        print("No dictionary files found.")
        exit(1)

    # Display the available dictionaries
    print("Available dictionaries:")
    for idx, dictionary in enumerate(available_dictionaries, 1):
        print(f"{idx}. {dictionary}")

    # Prompt the user to select a dictionary file
    try:
        choice = int(input("Select a dictionary file by entering the corresponding number: "))
        if 1 <= choice <= len(available_dictionaries):
            selected_dictionary = available_dictionaries[choice - 1]
        else:
            print("Invalid choice. Exiting.")
            exit(1)
    except ValueError:
        print("Invalid input. Exiting.")
        exit(1)

    # Prompt the user to enter the password to test
    password = input("Enter the password to test: ")

    # Perform the dictionary attack
    result = dictionary_attack(password, selected_dictionary)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
