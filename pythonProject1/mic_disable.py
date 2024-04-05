import pygetwindow as gw
import time
import sounddevice as sd

def ativar_microfone():
    try:
        mic = sd.InputStream()
        mic.start()
        print("Microfone ativado com sucesso.")
        return mic
    except Exception as e:
        print(f"Erro ao ativar o microfone: {e}")
        return None

def desativar_microfone(mic):
    if mic is None:
        print("O microfone já está desativado.")
        return

    mic.stop()
    mic.close()
    print("Microfone desativado com sucesso.")

# Exemplo de uso na main do programa
def main():
    # Ativar o microfone
    microfone = ativar_microfone()

    if microfone is not None:
        # Aguardar alguns segundos (simulando algum processamento)

        # Desativar o microfone
        desativar_microfone(microfone)

if __name__ == "__main__":
    main()
