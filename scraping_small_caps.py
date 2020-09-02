
from requests import get
from bs4 import BeautifulSoup

url_small_caps  = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=SMLL&idioma=pt-br'
carteira_small = []

browser = BeautifulSoup(get(url_small_caps).content, "html.parser")
base = browser.find('tbody').findAll('tr')
for tr_soup in base:
    td_soup = tr_soup.findAll('td')
    carteira_small.append(td_soup[1].text.replace('\n',''))
