# Let's now merge the file encryption and decryption functions into a class called EncryptionManager
# using the files file_encryption.py and file_decryption.py.

import file_encrypt as fileEncrypt # Import the file_encrypt module as fileEncrypt
import file_decrypt as fileDecrypt # Import the file_decrypt module as fileDecrypt
import os # Import the os module to get the directory of the input file

class EncryptionManager:
    def __init__(self):
        self.fileEncrypt: fileEncrypt = fileEncrypt
        self.fileDecrypt: fileDecrypt = fileDecrypt

    def encrypt_file(self):
        file_input: str = input("Enter the file to encrypt: ")

        # Check if the file exists
        if os.path.exists(file_input):

            # Get the output file path from the user
            file_output: str = input("Enter the output file (default is 'data.bin' in the original file directory): ")

            # Check if the output file path is empty
            if file_output == "" or not file_output:
                # If the output file path is empty, the encrypted file will be saved in the same directory as the input file
                # with the name "data.enc"
                # Get the directory of the input file
                directory: str = os.path.dirname(file_input)
                # Set the output file path to the same directory as the input file with the name "data.bin"
                file_output: str = os.path.join(directory, "data.bin")

            # Check if the output file already exists
            if os.path.exists(file_output):
                print(f"WARNING! The file '{file_output}' already exists.")
                answer: str = input("Do you want to overwrite it? The original file will be lost permanently. (yes/no): ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    # Encrypt the file using the file_encrypt module and the encrypt_file function
                    password = fileEncrypt.get_password()
                    fileEncrypt.encrypt_file(file_input, file_output, password)
        else:
            print(f"The file '{file_input}' was not found.")

    def decrypt_file(self):
        file_input = input("Enter the file path to decrypt: ")

        # Check if the file exists
        if os.path.exists(file_input):

            # Get the output file path from the user
            output_path = input("Enter the output path (default is the original file directory): ")
            # Check if the output file path is empty
            if output_path == "" or not output_path:
                # If output_path is empty, the decrypted file will be saved in the same directory as the input file
                # Set the output file path to the same directory as the input file
                output_path =os.path.dirname(file_input)
                # Decrypt the file using the file_decrypt module and the decrypt_file function
                key: bytes = fileDecrypt.get_key()  # Get the key from the user
                iv_base64, encrypted_file_name_base64, encrypted_content_base64 = fileDecrypt.read_encrypted_file(file_input)
                decrypted_results: tuple[str, str] = fileDecrypt.file_decrypt(key, iv_base64, encrypted_file_name_base64,
                                                      encrypted_content_base64, output_path)

                if decrypted_results:  # If the file has been decrypted successfully
                    print("The file has been decrypted successfully and saved to the file '" + decrypted_results[0] + "'")
                    # Print the hash (SHA256) of the decrypted file
                    print("The hash (SHA256) of the decrypted file is: " + decrypted_results[1])

        else:
            print(f"The file '{file_input}' was not found.")



def main():
    global encryptionManager
    encryptionManager = EncryptionManager()
    # Create an instance of the EncryptionManager class
    print("\nWelcome to the File Encryption Manager! https://github.com/Zorba1973")
    options_chooser()

def options_chooser() -> None:
    # Users can choose if they want encrypt or decrypt a file
    print("Please, select an option:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Help")
    print("4. Exit")

    # Get the option from the user
    option = input("Enter the option number: ")

    # Perform the encryption or decryption based on the user's choice
    if option == "1":
        encryptionManager.encrypt_file()
    elif option == "2":
        encryptionManager.decrypt_file()
    elif option == "3":
        help_functionality()
    else:
        print("Goodbye!")
        exit()
    print("\nWhat would you like to do next?")
    options_chooser()

def help_functionality() -> None:
    # Display the help information
    print("\nThis program allows you to encrypt and decrypt files using AES encryption.")
    print("The encryption is done using the AES algorithm in CBC mode with a 16-byte key and a random IV.")
    print("You can choose to encrypt a file by selecting option 1 and providing the file path.")
    print("You can choose to decrypt a file by selecting option 2 and providing the file path.")
    print("You can exit the program by selecting option 4.")
    print("For more information, visit: https://github.com/Zorba1973")

if __name__ == "__main__":
    main()











