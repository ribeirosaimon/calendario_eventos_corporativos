import csv

lista_de_resultados = []

def tratamento_dos_dados_da_b3():
    with open('cronograma.csv', 'r') as arquivo_csv:
        empresas = csv.reader(arquivo_csv, delimiter=',')
        for resultados in empresas:
            adicionando_empresas_a_lista(resultados[0],resultados[12])
            adicionando_empresas_a_lista(resultados[0],resultados[14])
            adicionando_empresas_a_lista(resultados[0],resultados[16])
    del(lista_de_resultados[0:10])
    return lista_de_resultados

def adicionando_empresas_a_lista(nome,data):
    nova_lista = []
    nova_lista.append(nome)
    nova_lista.append(data)
    lista_de_resultados.append(nova_lista)
    return None
