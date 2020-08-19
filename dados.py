import csv

def tratamento_datas():
    lista_de_resultados =[]
    with open('crono_2020.csv', 'r') as arquivo_csv:
        empresas = csv.reader(arquivo_csv, delimiter=',')
        for resultados in empresas:
            empresa = []
            empresa.append(resultados[0])
            empresa.append(resultados[12])
            empresa.append(resultados[14])
            empresa.append(resultados[16])
            lista_de_resultados.append(empresa)
    del(lista_de_resultados[0:12])
    return lista_de_resultados
