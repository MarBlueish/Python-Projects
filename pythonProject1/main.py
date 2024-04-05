import tkinter as tk
from PIL import Image, ImageTk
from network_shutdown import turn_on_wifi, turn_off_wifi
from camera_disable import desativar_webcam, ativar_webcam
from backup import fazer_backup
from mic_disable import ativar_microfone, desativar_microfone
import ctypes
import sys

# Definir source e destino para backup
source_path = "C:/Users/Marco/Downloads/Backup/MasterFile"
destination_path = "C:/Users/Marco/Downloads/Backup/BackupFile"

# Inicializar as variáveis globais para a webcam e o microfone
webcam = None
microfone = None

# Função para executar o programa com privilégios de administrador
def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Função para fechar a janela
def fechar_janela():
    global webcam, microfone
    if webcam is not None:
        desativar_webcam(webcam)
    if microfone is not None:
        desativar_microfone(microfone)
    janela.destroy()

# Função para desligar o adaptador de rede
def off_network():
    turn_off_wifi()

# Função para ligar adaptador de rede
def on_network():
    turn_on_wifi()

# Função para desativar microfone
def off_mic():
    global microfone
    desativar_microfone(microfone)

# Função de ligar microfone
def on_mic():
    global microfone
    microfone = ativar_microfone()

# Função de desligar webcam
def off_webcam():
    global webcam
    desativar_webcam(webcam)

# Função de ligar webcam
def on_webcam():
    global webcam
    webcam = ativar_webcam()

# Função para fazer backup
def do_backup():
    fazer_backup(source_path, destination_path)

# Criar a janela
janela = tk.Tk()

# Configurar o título da janela
janela.title("AntiVirus WebDev")

# Configurar as dimensões da janela
janela.geometry("878x360")

# Personalização Tkinter: Imagem de fundo
imagem_pillow = Image.open("C:/Users/Marco/Downloads/Backup/backgroundimage/cybersecurity.jpg")
background_image = ImageTk.PhotoImage(imagem_pillow)

label_imagem = tk.Label(janela, image=background_image)
label_imagem.place(x=0, y=0, relwidth=1, relheight=1)  # Cobrir toda a janela

# Configurar variáveis de controle para os botões de toggle
var_webcam = tk.IntVar()
var_network = tk.IntVar()
var_mic = tk.IntVar()

#botao webcam on
botao_webcam_on = tk.Button(janela, text="Ligar Webcam", command=on_webcam, bg="green")
botao_webcam_on.place(relx=0,rely=0,relwidth=0.15,relheight=0.15) #Mudar posicionamento x+y
#botao webcam off
botao_webcam_off = tk.Button(janela, text="Desligar Webcam", command=off_webcam, bg="red")
botao_webcam_off.place(relx=0,rely=0,relwidth=0.15,relheight=0.15) #Mudar posicionamento x+y
#botao network on
botao_network_on = tk.Button(janela, text="Ligar Adaptador de rede", command=on_network, bg="green")
botao_network_on.place(relx=0,rely=0,relwidth=0.15,relheight=0.15) #Mudar posicionamento x+y
#botao network off
botao_network_off = tk.Button(janela, text="Desligar Adaptador de rede", command=off_network, bg="red")
botao_network_off.place(relx=0,rely=0,relwidth=0.15,relheight=0.15) #Mudar posicionamento x+y
# botao mic on
botao_mic_on = tk.Button(janela, text="Ligar Microfone", command=on_mic, bg="green")
botao_mic_on.place(relx=0,rely=0,relwidth=0.15,relheight=0.15) # mudar posicionamento x e y
#botao mic off
botao_mic_off = tk.Button(janela, text="Desligar Microfone", command=off_mic, bg="red")
botao_mic_off.place(relx=0.0001,rely=0.0001,relwidth=0.15,relheight=0.15) # posição de botão um, em primeiro lugar, podemos alterar dps
# Botão de backup normal
botao_backup = tk.Button(janela, text="Fazer Backup", command=do_backup, bg="grey")
botao_backup.place(relx=0.8,rely=0.85,relwidth=0.10,relheight=0.15)
# Criar o botão "Fechar", define tamanho e posiciona o botão a direita
botao_fechar = tk.Button(janela, text="Fechar", command=fechar_janela)
botao_fechar.place(relx=0.9,rely=0.85,relwidth=0.10,relheight=0.15)
# Iniciar o loop principal da janela
janela.mainloop()
