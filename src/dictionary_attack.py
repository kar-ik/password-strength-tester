import os
import time
from tqdm import tqdm

def dictionary_attack(password, dictionary_file):
    if not os.path.exists(dictionary_file):
        print(f"Dictionary file {dictionary_file} not found.")
        return None

    with open(dictionary_file, 'r') as file:
        lines = file.readlines()

    # Start the progress bar
    with tqdm(total=len(lines), desc="Processing") as pbar:
        for line in lines:
            if line.strip() == password:
                return password
            pbar.update(1)
    return None

if __name__ == "__main__":
    
    dictionaries = ["indianpass-list.txt", "uspass-list.txt", "10000000pass-list.txt"]

    available_dictionaries = [d for d in dictionaries if os.path.exists(d)]
    if not available_dictionaries:
        print("No dictionary files found.")
        exit(1)

    
    print("Available dictionaries:")
    for idx, dictionary in enumerate(available_dictionaries, 1):
        print(f"{idx}. {dictionary}")

    
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

    
    password = input("Enter the password to test: ")

    
    start_time = time.time()
    result = dictionary_attack(password, selected_dictionary)
    end_time = time.time()

    
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
