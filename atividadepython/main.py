
# import json

# Abra o arquivo JSON para leitura
# with open("population.json", "r") as arquivo:
#    data = json.load(arquivo)

# Acesse a lista de países no arquivo JSON
# lista_de_paises = data

# Encontre o país com a menor população
# pais_com_menor_populacao = min(lista_de_paises, key=lambda pais: pais["population"])

# Encontre o país com a maior população
# pais_com_maior_populacao = max(lista_de_paises, key=lambda pais: pais["population"])

# print(f"País com a menor população: {pais_com_menor_populacao['country']} ({pais_com_menor_populacao['population']} habitantes)")
# print(f"País com a maior população: {pais_com_maior_populacao['country']} ({pais_com_maior_populacao['population']} habitantes)")


import json


# Função para formatar a população com pontos e vírgulas

def formatar_populacao(populacao):
    return '{:,}'.format(populacao).replace(',', '.')


# Abra o arquivo JSON para leitura
with open("people.json", "r") as arquivo:
    data = json.load(arquivo)

# Acesse a lista de países no arquivo JSON
lista_de_paises = data

# Ordene a lista de países pelo nome
lista_de_paises_ordenada_por_nome = sorted(lista_de_paises, key=lambda pais: pais["country"])

# Encontre o país com a menor população usando lambda
pais_com_menor_populacao = min(lista_de_paises, key=lambda pais: pais["population"])

# Encontre o país com a maior população usando lambda
pais_com_maior_populacao = max(lista_de_paises, key=lambda pais: pais["population"])

print("Países ordenados pelo nome:")
for pais in lista_de_paises_ordenada_por_nome:
    print(f"País: {pais['country']}, População: {formatar_populacao(pais['population'])} habitantes")

print(
    f"\nPaís com população mínima: {pais_com_menor_populacao['country']} ({formatar_populacao(pais_com_menor_populacao['population'])} habitantes)")
print(
    f"País com população máxima: {pais_com_maior_populacao['country']} ({formatar_populacao(pais_com_maior_populacao['population'])} habitantes)")

