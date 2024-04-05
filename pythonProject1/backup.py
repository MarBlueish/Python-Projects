import os
import shutil
import zipfile
from datetime import datetime

def fazer_backup(source, destino):
    try:
        # Criar um nome único para o arquivo de backup usando a data e hora atual
        data_hora = datetime.now().strftime("%Y%m%d%H%M%S")
        nome_backup = f"backup_{data_hora}.zip"

        # Adicionar a data e hora ao caminho de destino
        destino = os.path.join(destino, nome_backup)

        # Criar um arquivo ZIP para o backup
        with zipfile.ZipFile(destino, 'w') as zipf:
            # Recursivamente adiciona todos os arquivos/diretórios ao ZIP
            for root, dirs, files in os.walk(source):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, source))

        print("Backup concluído com sucesso!")

    except Exception as e:
        print(f"Erro ao fazer backup: {e}")

# Define os caminhos de origem e destino
source = 'C:/Users/Marco/Downloads/Backup/MasterFile'
destino ='C:/Users/Marco/Downloads/Backup/BackupFile'

# Chama a função de backup
fazer_backup(source, destino)
