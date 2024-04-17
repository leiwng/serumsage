from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the username and password
username = "my_username"
password = "my_password"

encrypted_username = cipher_suite.encrypt(username.encode())
encrypted_password = cipher_suite.encrypt(password.encode())

# Save the encrypted username and password to a file
with open("credentials.txt", "wb") as file:
    file.write(encrypted_username + b"\n")
    file.write(encrypted_password)

# Read the encrypted username and password from the file
with open("credentials.txt", "rb") as file:
    encrypted_username = file.readline().strip()
    encrypted_password = file.readline().strip()

# Decrypt the username and password
decrypted_username = cipher_suite.decrypt(encrypted_username).decode()
decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

print("Username:", decrypted_username)
print("Password:", decrypted_password)