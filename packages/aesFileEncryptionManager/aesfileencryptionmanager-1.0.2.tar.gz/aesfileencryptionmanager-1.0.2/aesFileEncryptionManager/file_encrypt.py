# Let's now encrypt a file using the AES algorithm in Python using the pycryptodome library.
# The following code shows how to encrypt a file using the AES algorithm and base64 encoding:

# Import the necessary libraries
from getpass import getpass # Import the getpass function to hide the password
from Crypto.Cipher import AES # Import the AES algorithm
from Crypto.Random import get_random_bytes # Import the random bytes generator
from Crypto.Util.Padding import pad # Import the padding function
from Crypto.Hash import SHA256 # Import the SHA256 algorithm
import os # Import the os module to get the file size
import sys # Import the sys module to get the command-line arguments
from base64 import b64encode # Import the base64 encoding function


# Ask the user for the password
def get_password() -> str:
    user_password: str = getpass("Enter the password to encrypt the file: ")
    password_confirmation: str = getpass("Confirm the password: ")
    if user_password != password_confirmation:
        print("The passwords do not match. Try again.")
        return get_password()
    return user_password

# Function to encrypt a file using the AES algorithm and base64 encoding
def encrypt_file(file_input: str, file_output: str, password: str) -> None:
    # The password will be hashed to get a key of 32 bytes
    key: bytes = SHA256.new(password.encode()).digest() # Hash the password to get a key of 32 bytes

    # Generate a random initialization vector (IV) of 16 bytes
    iv: bytes = get_random_bytes(16)

    # Create an AES cipher object with the key and the mode of operation
    cipher: AES = AES.new(key, AES.MODE_CBC, iv)

    # Read the file to encrypt
    try: # Try to open the file to read the content
        with open(file_input, "rb") as file:
            file_content: bytes = file.read()
            # Print the hash (SHA256) of the original file
            print("The hash (SHA256) of the file to be encrypted is:", SHA256.new(file_content).hexdigest())
    except(FileNotFoundError, IOError):
        print(f"The file '{file_input}' was not found or there was an error while reading the file.")
        print("Goodbye!")
        exit()

    # Read the file name and file name length
    file_name = os.path.basename(file_input)

    # Encrypt the file name using the cipher object and the IV
    encrypted_file_name: bytes = cipher.encrypt(pad(file_name.encode(), AES.block_size))

    # Pad the file content to be a multiple of 16 bytes
    padded_content: bytes = pad(file_content, AES.block_size)

    # Encrypt the file content using the cipher object
    encrypted_content: bytes = cipher.encrypt(padded_content)

    # Convert the IV, the encrypted file name, and the encrypted content to base64 strings
    iv_base64: str = b64encode(iv).decode() # The length of the IV is 24 bytes because it is a base64 string calculated from 16 bytes (16 * 4 / 3 = 24)
    encrypted_content_base64: str = b64encode(encrypted_content).decode()
    encrypted_file_name_base64: str = b64encode(encrypted_file_name).decode()

    # Write the IV and the encrypted content to a file
    with open(file_output, "w") as file:
        file.write(iv_base64) # Write the IV to the file to be used in the decryption (24 bytes because it is a base64 string calculated from 16 bytes)
        file.write(encrypted_file_name_base64) # Write the encrypted file name to the file after the IV
        file.write("\n") # Add a new line to separate the line with the IV and the encrypted file name from the encrypted content
        file.write(encrypted_content_base64) # Write the encrypted content to the file after the IV and the encrypted file name
    print(f"The file has been encrypted successfully and saved to '{file_output}'")
    print("Do not forget the password or you will not be able to decrypt the file.")
    answer = input("Do you want to print the password on the screen? (yes/no): ")
    if answer.lower() == "yes" or answer.lower() == "y":
        print(f"The password is: {password}. Keep it safe and do not lose it.") # Print the password on the screen

def main():
    # Get the file path from the command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <file_path> <output_path>")
        exit()

    file_path: str = sys.argv[1]  # Get the file path from the command-line arguments
    output_path: str = sys.argv[2]  # Get the output path from the command-line arguments

    # Check if the file output_path already exists
    if os.path.exists(output_path):
        print(f"The file '{output_path}' already exists.")
        answer = input("Do you want to overwrite it? (yes/no): ")
        if answer.lower() != "yes" and answer.lower() != "y":
            print("Goodbye!")
            exit()
    password = get_password()
    encrypt_file(file_path, output_path, password)

if __name__ == "__main__":
    main()
