import pytesseract
import cv2
import re
import shutil
import os

# Caminho Tesseract
caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract

# Pasta dos arquivos para renomear
pasta_arquivo = r"C:\Users\guigu\OneDrive\GUI\Gui_read\arquivos"

# Pasta destino dos arquivos renomaedos
pasta_destino = r"C:\Users\guigu\OneDrive\GUI\Gui_read\renomeados"

# Lista os arquivos na pasta renomear
lista_arquivos = os.listdir(pasta_arquivo)

for arquivo in lista_arquivos:
    # Verifica se o arquivo é uma imagem
    if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):

        # Caminho completo para a imagem
        caminho_imagem = os.path.join(pasta_arquivo, arquivo)
        
        # Carrega a imagem usando o OpenCV
        imagem = cv2.imread(caminho_imagem)
        
        # Converte a imagem para escala de cinza (Simplifica a transformação da imagens para texto)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        
        # Extrai texto por meio do tesseract
        texto = pytesseract.image_to_string(imagem_cinza)
        
        # Extrai no texto da imagem o número da NF
        numero_nf = re.search(r'(N[°®] (\d+\.\d+\.\d+))', texto)
        
        # Condições se entrar ou não encontrar o numero da NF
        if numero_nf:

            numero_nf_extraido = numero_nf.group(1)
            
            # Nome do novo arquivo
            novo_nome_renomeado = f"NF-{numero_nf_extraido}.png"
            
            # Salva o arquivo renomeado na pasta renomeados
            salvando_renomeado = os.path.join(pasta_destino, novo_nome_renomeado)
            
            # Salva uma cópia com o número extraido
            shutil.copy(caminho_imagem, salvando_renomeado)
            
            # Exclui a imagem original na pasta arquivos
            os.remove(caminho_imagem)

            # Print no terminal
            print(f"NF 000-{numero_nf_extraido} - Renomeada!")
            print(f"Salvando {salvando_renomeado}")
            print(f"Imagem {caminho_imagem} removida")
            print(f"")

        else:
            print(f"Arquivo {arquivo} nao lido!")
            print(f"")
