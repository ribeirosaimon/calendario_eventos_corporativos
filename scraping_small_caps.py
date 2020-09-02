from requests import get
from bs4 import BeautifulSoup
import time

url_small_caps  = 'http://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-small-cap-smll-composicao-da-carteira.htm'
time.sleep(5)
browser = BeautifulSoup(get(url_small_caps).content, "html.parser")
base = browser.find('tbody')
print(base)
