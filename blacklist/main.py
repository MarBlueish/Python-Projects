import socket

# Pede IPv4 ao usuário
host_name = socket.gethostname()

# Guarda o próprio IPv4 do usuário
ipv4_address = socket.gethostbyname(host_name)


# Lista de IPs banidos
blacklist_ips = ["XXX.XXX.XX.XX", "XX.X.X.X", "XXX.X.X.XX", "XXX.X.X.XXX", "XXX.X.XXX.XX"]

# Funcionalidade de comparação
if ipv4_address in blacklist_ips:
    print("You have been banned from the server.")
else:
    print("Welcome!")

