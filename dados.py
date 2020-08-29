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
    data = data[:10].split('-')
    if len(data) != 3:
        data = 'cabeçalho'
    else:
        if data[1][0] == '0':
            data[1] = data[1].replace('0','')
        if data[2][0] == '0':
            data[2] = data[2].replace('0','')
        data = f'{data[1]}/{data[2]}/{data[0]}'
    nova_lista.append(nome)
    nova_lista.append(data)
    lista_de_resultados.append(nova_lista)
    return None
