import sys
import pprint
from shutil import which
import os
import gnupg
file_path = 'C:\\Users\\Marco\\PycharmProjects\\tarefa01py\\my_generated_key.asc'


try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        # You can now work with the contents of the file as needed
        print(file_contents)
except FileNotFoundError:
    print(f"File not found at {file_path}")

#Example: python3 decrypt_file.py name_of_file.txt passphrase
gpg = gnupg.GPG('C:\\Program Files (x86)\\GNU\\GnuPG\\bin\\gpg.exe')
gpg.encoding = 'utf8'
key_input_data = gpg.gen_key_input(
    name_email='test',
    passphrase='test',
    key_type='RSA',
    key_length=4096
)
key = gpg.gen_key(key_input_data)

with open('my_generated_key.asc', 'w') as key_file:
    key_file.read(int('my_generated_key.asc'))
if which('gpg') is None:
    sys.exit("Please install gnupg in Windows")
gpg = gnupg.GPG()
with open (sys.argv[1], 'rb') as f:
    status = gpg.decrypt_file(
             file="test",
             passphrase="test",
             output=("decrypted-")
           )

    print('ok: ', status.ok)
    print('status: ', status.status)
    print('stderr: ', status.stderr)