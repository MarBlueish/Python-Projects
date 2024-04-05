import tkinter as tk
from pynput import mouse, keyboard
import cv2
import ctypes
import os
from PIL import Image, ImageTk

# Obtenha o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construa o caminho para o diretório de destino (área de trabalho)
dest_dir = os.path.join(script_dir, 'C:\\Users\\Marco\\Desktop\\teste')

# Certifique-se de que o diretório de destino existe
os.makedirs(dest_dir, exist_ok=True)

# Função para bloquear o computador e tirar uma foto
def lock_and_capture():
    # Bloquear o computador (mesmo código que anteriormente)
    root.withdraw()
    root.after(400, lambda: root.iconify())
    root.after(600, lambda: root.destroy())
    ctypes.windll.user32.LockWorkStation()

    # Capturar uma foto da câmera
    _, frame = cap.read()

    # Construa o caminho completo para a foto com um nome de arquivo exclusivo
    photo_path = os.path.join(dest_dir, 'printscreen_invasor.jpg')

    # Adicione prints para depuração
    print("Salvando foto em:", photo_path)
    success = cv2.imwrite(photo_path, frame)
    if success:
        print("Foto salva com sucesso!")
    else:
        print("Erro ao salvar a foto.")

# Função chamada quando qualquer tecla é pressionada
def on_key_press(key):
    lock_and_capture()

# Função chamada quando o mouse é movido
def on_mouse_move(x, y):
    lock_and_capture()

# Inicializar a câmera (mesmo código que anteriormente)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

# Configurar a janela principal (mesmo código que anteriormente)
root = tk.Tk()
root.title("Cão Guarda")

# Define o tamaho da janela
root.geometry("400x300")

# Definir imagem que vai aparecer dentro do tkinter(?)
image_path = "C:\\Users\\Marco\\Desktop\\teste\\caopolicia.jpg"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)

# Configurar a janela para detectar eventos de teclado (mesmo código que anteriormente)
keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()

# Configurar a janela para detectar eventos de mouse (mesmo código que anteriormente)
mouse_listener = mouse.Listener(on_move=on_mouse_move)
mouse_listener.start()

# Iniciar loop principal da interface gráfica (mesmo código que anteriormente)
root.mainloop()

# Liberar os recursos quando terminar
cap.release()
cv2.destroyAllWindows()


