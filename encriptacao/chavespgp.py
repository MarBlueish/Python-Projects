import gnupg

# inicia o objeto
gpg = gnupg.GPG()

# cria 2 chaves pgp
dados_input = gpg.gen_key_input(
    name_real='Seu Nome',
    name_email='seu@email.com',
    passphrase='sua-senha-secreta'
)

chave = gpg.gen_key(dados_input)

# da print na chave
print("Impressão digital da chave:", chave.fingerprint)
