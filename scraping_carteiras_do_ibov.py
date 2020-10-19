from requests import get
from bs4 import BeautifulSoup
import time

url_small_caps  = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=SMLL&idioma=pt-br'
url_ibov = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=ibov&idioma=pt-br'


def scraping_carteiras():
    lista_carteira = []
    time.sleep(2)
    browser = BeautifulSoup(get(url_small_caps).content, "html.parser")
    time.sleep(2)
    base = browser.find('tbody').findAll('tr')
    for tr_soup in base:
        td_soup = tr_soup.findAll('td')
        lista_carteira.append(td_soup[1].text.replace('\n',''))
    time.sleep(2)
    browser = BeautifulSoup(get(url_ibov).content, "html.parser")
    time.sleep(2)
    base = browser.find('tbody').findAll('tr')
    for tr_soup in base:
        td_soup = tr_soup.findAll('td')
        lista_carteira.append(td_soup[1].text.replace('\n',''))
    print(lista_carteira)
    return lista_carteira
