# Let's now decrypt the file using the AES algorithm in Python using the pycryptodome library.
# The following code shows how to decrypt a file using the AES algorithm and base64 encoding:

# Import the necessary libraries
from getpass import getpass # Import the getpass function to hide the password
from Crypto.Cipher import AES # Import the AES algorithm
from Crypto.Util.Padding import unpad # Import the unpadding function
from Crypto.Hash import SHA256 # Import the SHA256 algorithm
import os # Import the os module to get the file size
import sys # Import the sys module to get the command-line arguments
from base64 import b64decode # Import the base64 decoding function

# Function to get the password from the user and hash it to get a key of 32 bytes
def get_key() -> bytes:
    user_password: str = getpass("Enter the password: ") # Ask the user for the password
    key: bytes = SHA256.new(user_password.encode()).digest()  # Hash the password to get a key of 32 bytes
    return key

# Function to get the IV, the encrypted file name, and the encrypted content from the file
def read_encrypted_file(file_input: str) -> tuple[str, str, str]:
    try: # Try to open the file to read the encrypted content
        # Open the file to read the IV, the encrypted file name, and the encrypted content
        with open(file_input, "r") as file:
            # First line contains the IV and the encrypted file name
            first_line: str = file.readline().strip()
            # Split the first line into the IV and the encrypted file name
            # First 24 characters are the IV and the rest is the encrypted file name
            iv_base64: str = first_line[:24] # Read the IV from the file (24 bytes, because it is a base64 string calculated from 16 bytes)
            encrypted_file_name_base64: str = first_line[24:] # Read the encrypted file name from the file after the IV
            # The rest of the file (the second line and the rest) is the encrypted content
            encrypted_content_base64: str = file.read()
            return iv_base64, encrypted_file_name_base64, encrypted_content_base64
    # If the file does not exist or there is an error while reading the file FileNotFoundError or IOError will be raised
    except(FileNotFoundError, IOError):
        print(f"The file '{file_input}' was not found or there was an error while reading the file.")
        exit()

# Function to decrypt the file using the key, the IV, the encrypted file name, and the encrypted content
def get_decrypted_file(key, iv_base64, encrypted_file_name_base64, encrypted_content_base64, output_path: str) -> str | None:
    try:
        # Convert the IV, the encrypted file name, and the encrypted content from base64 to bytes
        iv: bytes = b64decode(iv_base64)
        encrypted_file_name: bytes = b64decode(encrypted_file_name_base64)
        encrypted_content: bytes = b64decode(encrypted_content_base64)

        # Create an AES cipher object with the key, the mode of operation and the IV
        cipher: AES = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the file name using the cipher object
        decrypted_file_name: bytes = unpad(cipher.decrypt(encrypted_file_name), AES.block_size)

        # Decrypt the file content using the cipher object
        decrypted_content: bytes = unpad(cipher.decrypt(encrypted_content), AES.block_size)

        # Operation to save the decrypted file
        file_name, file_extension = os.path.splitext(decrypted_file_name.decode()) # Split the file name and the extension: file_name, file_extension
        file_name += "_decrypted" + file_extension # Add "_decrypted" to the file name: file_name_decrypted.extension
        # Join the output path and the file name: output_path/file_name.extension
        file_name = os.path.join(output_path, file_name)
        # Check if the file already exists
        if os.path.exists(file_name):
            print(f"The file '{file_name}' already exists.")
            answer = input("Do you want to overwrite it? (yes/no): ")
            if answer.lower() != "yes" and answer.lower() != "y":
                print("Goodbye!")
                exit()
        # Write the decrypted content to the file
        with open(file_name, "wb") as file:
            file.write(decrypted_content)
        return file_name
    except ValueError:
        # If the password is incorrect, the decryption will fail
        print("Please check the password: it seems to be incorrect.")
        return None

def file_decrypt(key: bytes, iv_base64: str, encrypted_file_name_base64: str,
                 encrypted_content_base64: str, output_path: str) -> tuple[str, str] | None:
    try:
        # Convert the IV, the encrypted file name, and the encrypted content from base64 to bytes
        iv: bytes = b64decode(iv_base64)
        encrypted_file_name: bytes = b64decode(encrypted_file_name_base64)
        encrypted_content: bytes = b64decode(encrypted_content_base64)

        # Create an AES cipher object with the key, the mode of operation and the IV
        cipher: AES = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the file name using the cipher object
        decrypted_file_name: bytes = unpad(cipher.decrypt(encrypted_file_name), AES.block_size)

        # Decrypt the file content using the cipher object
        decrypted_content: bytes = unpad(cipher.decrypt(encrypted_content), AES.block_size)

        # Operation to save the decrypted file
        file_name, file_extension = os.path.splitext(decrypted_file_name.decode()) # Split the file name and the extension: file_name, file_extension
        file_name += "_decrypted" + file_extension # Add "_decrypted" to the file name: file_name_decrypted.extension
        # Join the output path and the file name: output_path/file_name.extension
        file_name = os.path.join(output_path, file_name)
        # Check if the file already exists
        if os.path.exists(file_name):
            print(f"The file '{file_name}' already exists.")
            answer = input("Do you want to overwrite it? (yes/no): ")
            if answer.lower() != "yes" and answer.lower() != "y":
                return None
        # Write the decrypted content to the file
        with open(file_name, "wb") as file:
            file.write(decrypted_content)
        # Return the file name and the hash (SHA256) of the decrypted content
        return file_name, SHA256.new(decrypted_content).hexdigest()
    except ValueError:
        # If the password is incorrect, the decryption will fail
        print("Please check the password: it seems to be incorrect.")
        return None



# Main function
def main():
    # Get the file path from the command-line arguments
    if len(sys.argv) <2 or len(sys.argv) > 3:
        print("Usage: python file_decrypt.py <file_to_decrypt> [output_path]")
        print("The output_path is optional. If not provided, the decrypted file will be saved in the current directory.")
        print("Example: python file_decrypt.py encrypted_file.txt decrypted_files")
        print("Example: python file_decrypt.py encrypted_file.txt")
        exit()
    # Get the file_to_decrypt from the command-line arguments
    file_to_decrypt: str = sys.argv[1]
    if len(sys.argv) == 3:
        output_path: str = sys.argv[2]
    else:
        # If the output path is not provided, use the current directory
        output_path: str = os.getcwd()
    # Read the IV, the encrypted file name, and the encrypted content from the file
    iv_base64, encrypted_file_name_base64, encrypted_content_base64 = read_encrypted_file(file_to_decrypt)
    # Get the key from the user
    key: bytes = get_key()  # Get the key from the user
    # Decrypt the file using the key, the IV, the encrypted file name, and the encrypted content
    output_file_name = get_decrypted_file(key, iv_base64, encrypted_file_name_base64, encrypted_content_base64, output_path)
    if output_file_name: # If the file has been decrypted successfully
        print("The file has been decrypted successfully and saved to the file '" + output_file_name + "'")
        # Print the hash (SHA256) of the decrypted file
        with open(output_file_name, "rb") as file:
            print("The hash (SHA256) of the decrypted file is: " + SHA256.new(file.read()).hexdigest())
    else:
        answer = input("Do you want to try again? (yes/no): ") # Ask the user if they want to try again
        if answer.lower() == "yes" or answer.lower() == "y":
            main()
        else:
            print("Goodbye!")
            exit()

if __name__ == "__main__":
    main()
