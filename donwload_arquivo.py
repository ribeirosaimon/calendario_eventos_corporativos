import requests
import os
import pandas as pd
from dados import *

def convert_xlsx(nome_arquivo, nome_convertido):
    df = pd.read_excel(nome_arquivo)
    df.to_csv(nome_convertido+'.csv', index=False)
    os.remove(nome_arquivo)

def baixar_arquivo(url, endereco=None):
    if endereco is None:
        endereco = os.path.basename(url.split("?")[0])
        resposta = requests.get(url, stream=True) #AQUI
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): #AQUI TBM
                    novo_arquivo.write(parte)
    else:
        resposta.raise_for_status()
    convert_xlsx(endereco, 'cronograma')
