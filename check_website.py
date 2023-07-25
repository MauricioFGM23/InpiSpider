import requests
from bs4 import BeautifulSoup

def check_url_availability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

def check_website(url):
    if not check_url_availability(url):
        print("Servidor fora do ar! Verifique a conexão ou aguarde o retorno.")
        return

    print("O site está acessível!")

    # Exemplo adicional: Extrair o título da página usando BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').get_text()
    print("Título da página:", title, "\n")

# start_urls = ["https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login"]
# check_website(start_urls[0])