import requests
import os
from pathlib import Path

def download(url, destino_usr=None):

    nome_arquivo = os.path.basename(url.split("?")[0])

    if destino_usr is not None:
        caminho_arquivo = Path(destino_usr) / nome_arquivo #caminho passado pelo usuário
    else:
        caminho_arquivo = nome_arquivo #caso não passe salva no diretório atual

    
    resposta = requests.get(url, stream=True)
    if resposta.status_code == requests.codes.OK:
        with open(caminho_arquivo, 'wb') as novo_arquivo:
            for parte in resposta.iter_content(chunk_size=256):
                novo_arquivo.write(parte)
        print("Terminou de Baixar. Arquivo salvo em: {}".format(caminho_arquivo))
        return True
    else:
        resposta.raise_for_status()
        return False

#destino = 'downloads'
#teste_url='https://fatweb.s3.amazonaws.com/vestibularfatec/documentos/2SEM-25/ManualCandidato.pdf?id=202521'
#download(teste_url, destino)