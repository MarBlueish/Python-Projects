import cv2
import pygetwindow as gw
import time

def ativar_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao abrir a webcam.")
        return None

    print("Webcam ativada com sucesso.")
    return cap

def desativar_webcam(cap, camera_window=None):
    if cap is None or not cap.isOpened():
        print("A webcam já está desativada.")
        return

    if camera_window is not None:
        camera_window.minimize()
        time.sleep(1)

    cap.release()
    print("Webcam desativada com sucesso.")

# Exemplo de uso na main do programa
def main():
    # Ativar a webcam
    webcam = ativar_webcam()

    if webcam is not None:
        # Aguardar alguns segundos (simulando algum processamento)

        # Desativar a webcam
        desativar_webcam(webcam)

if __name__ == "__main__":
    main()
