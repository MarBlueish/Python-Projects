import gnupg
from encrypt import encrypt


# Specify the path to GPG executable
gpg = gnupg.GPG('C:\\Program Files (x86)\\GNU\\GnuPG\\bin\\gpg.exe')
gpg.encoding = 'utf8'

# Specify the relative path to the key file
key_file_path = 'my_generated_key.asc'

# Read the PGP key from the text file
with open(key_file_path, 'r') as key_file:
    key_data = key_file.read()

# Import the key to the keyring
import_result = gpg.import_keys(key_data)

if import_result.count:
    print(f"Imported {import_result.count} key(s) to the keyring.")
else:
    print(f"Key import failed. Make sure '{key_file_path}' contains a valid PGP key.")

