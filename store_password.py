from cryptography.fernet import Fernet

# Generate and save a key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("key.key", "rb").read()

# Encrypt and store the password
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    with open("passwords.txt", "ab") as file:
        file.write(encrypted_password + b'\n')

if __name__ == "__main__":
    write_key()
    password = input("Enter the password to store: ")
    encrypt_password(password)
    print("Password stored securely")
