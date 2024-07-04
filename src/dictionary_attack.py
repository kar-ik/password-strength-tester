import os

def dictionary_attack(password, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            if line.strip() == password:
                return password
    return None

if __name__ == "__main__":
    dictionaries = ["indianpass.txt", "uspass.txt", "30000000pass.txt"]
    
    print("Available dictionaries:")
    for idx, dictionary in enumerate(dictionaries, 1):
        print(f"{idx}. {dictionary}")
    
        choice = int(input("Select a dictionary file by entering the corresponding number: "))
    if 1 <= choice <= len(dictionaries):
        selected_dictionary = dictionaries[choice - 1]
    else:
        print("Invalid choice. Exiting.")
        exit(1)
    
    password = input("Enter the password to test: ")
   
    result = dictionary_attack(password, selected_dictionary)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
