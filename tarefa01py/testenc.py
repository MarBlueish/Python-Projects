import gnupg

# PATH TO GPG
gpg = gnupg.GPG('C:\\Program Files (x86)\\GNU\\GnuPG\\bin\\gpg.exe')
gpg.encoding = 'utf8'

key_input_data = gpg.gen_key_input(
    name_email='test',
    passphrase='test',
    key_type='RSA',
    key_length=4096
)

key = gpg.gen_key(key_input_data)
print(key)

# Save the key to a text file
with open('my_generated_key.asc', 'w') as key_file:
    key_file.write(str(key))

print("Key has been generated and saved to my_generated_key.asc")

# Export the key to a file
exported_key = gpg.export_keys(key.fingerprint)

with open('exported_key.asc', 'w') as exported_key_file:
    exported_key_file.write(exported_key)

print("Key has been exported and saved to exported_key.asc")
