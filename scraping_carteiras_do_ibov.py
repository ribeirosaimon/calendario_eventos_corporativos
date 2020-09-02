from requests import get
from bs4 import BeautifulSoup

url_small_caps  = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=SMLL&idioma=pt-br'
url_ibov = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=ibov&idioma=pt-br'


def scraping_carteiras():
    lista_carteira = []
    browser = BeautifulSoup(get(url_small_caps).content, "html.parser")
    base = browser.find('tbody').findAll('tr')
    for tr_soup in base:
        td_soup = tr_soup.findAll('td')
        lista_carteira.append(td_soup[1].text.replace('\n',''))
    browser = BeautifulSoup(get(url_ibov).content, "html.parser")
    base = browser.find('tbody').findAll('tr')
    for tr_soup in base:
        td_soup = tr_soup.findAll('td')
        lista_carteira.append(td_soup[1].text.replace('\n',''))
    return lista_carteira
