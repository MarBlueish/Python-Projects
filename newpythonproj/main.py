import json
from cryptography.fernet import Fernet

def gerar_ou_carregar_chave(nome_arquivo_chave):
    try:
        with open(nome_arquivo_chave, 'rb') as arquivo_chave:
            chave = arquivo_chave.read()
    except FileNotFoundError:
        chave = Fernet.generate_key()
        with open(nome_arquivo_chave, 'wb') as arquivo_chave:
            arquivo_chave.write(chave)

    return chave

def gravar_arquivo_json(nome_arquivo, dados, chave):
    f = Fernet(chave)
    conteudo_json = json.dumps(dados).encode('utf-8')
    conteudo_cifrado = f.encrypt(conteudo_json)

    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(conteudo_cifrado)

def ler_arquivo_json(nome_arquivo, chave):
    with open(nome_arquivo, 'rb') as arquivo:
        conteudo_cifrado = arquivo.read()

    f = Fernet(chave)
    conteudo_decifrado = f.decrypt(conteudo_cifrado)

    conteudo_json = json.loads(conteudo_decifrado.decode('utf-8'))
    return conteudo_json

# Exemplo de uso:
nome_arquivo_chave = 'chave.key'
nome_arquivo = 'arquivo_cifrado.json'

# Gere ou carregue a chave
chave = gerar_ou_carregar_chave(nome_arquivo_chave)

# Pergunte ao usuário se deseja gravar ou ler
operacao = input("Deseja gravar ou ler? ").lower()

if operacao == 'gravar':
    dados_para_gravar = {'nome': 'Marco', 'idade': 23, 'cidade': 'Lisboa'}
    gravar_arquivo_json(nome_arquivo, dados_para_gravar, chave)
    print("Dados gravados com sucesso!")
elif operacao == 'ler':
    dados_lidos = ler_arquivo_json(nome_arquivo, chave)
    print("Dados lidos do arquivo JSON:", dados_lidos)
else:
    print("Operação inválida. Escolha 'gravar' ou 'ler'.")
