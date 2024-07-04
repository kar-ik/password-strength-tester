import os

def dictionary_attack(password, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            if line.strip() == password:
                return password
    return None

if __name__ == "__main__":
    dictionaries = ["indianpass.txt", "uspass.txt", "30000000pass.txt"]
    
    # Display the available dictionaries
    print("Available dictionaries:")
    for idx, dictionary in enumerate(dictionaries, 1):
        print(f"{idx}. {dictionary}")
    
    # Prompt the user to select a dictionary file
    choice = int(input("Select a dictionary file by entering the corresponding number: "))
    if 1 <= choice <= len(dictionaries):
        selected_dictionary = dictionaries[choice - 1]
    else:
        print("Invalid choice. Exiting.")
        exit(1)
    
    # Prompt the user to enter the password to test
    password = input("Enter the password to test: ")
    
    # Perform the dictionary attack
    result = dictionary_attack(password, selected_dictionary)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
