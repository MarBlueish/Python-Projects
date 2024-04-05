import keyboard
import socket

hostname = socket.gethostname()
ipv4_address = socket.gethostbyname(hostname)

print("Endereço IPv4 do usuário:", ipv4_address)
# Define user and pass
def user_corr_us():
    return "win"
def user_corr_ps():
    return ("win")

# Welcome message
print("Bem-vindo " ,ipv4_address ,"ao sistema de criptografia")
print("Por favor, insira as suas credenciais")

user_user = input("Insira o seu nome de utilizador: ")
user_pass = input("Insira a sua password: ")

# Verify username and password
if user_user == user_corr_us() and user_pass == user_corr_ps():
    print("Bem-vindo ao sistema")
elif user_user != user_corr_us() or user_pass != user_corr_ps():
    print("As credenciais estão erradas")


