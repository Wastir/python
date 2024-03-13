# Napisz dla Amazona program, który automatycznie wyciąga wybrane informacje z wybranych stron internetowych, na przykład nazwy produktów ze stron Leroy Merlin. Użytkownik podaje jedynie adres strony oraz ścieżkę xpath, którą może łatwo skopiować w przeglądarce.

# 1. Użyj biblioteki click, aby łatwiej było Ci odczytać url oraz xpath.

# 2. Podziel kod na funkcje tak, aby można było go łatwo testować.

# 3. Napisz kilka testów. Zacznij od tzw. happy path, tzn. najprostszego przypadku, a następnie przetestuj przypadki brzegowe.

# 4. Wyciągając z HTML tekst, usuń białe znaki z początku i końca (poszukaj odpowiedniej metody na stringach) oraz zamień znaki końca linii na spacje.

# 5. Wyświetl każdy znaleziony element HTML w osobnej linii.

# 6. Użyj docstringów, aby udokumentować Twój kod. Jakie informacje Twoim zdaniem warto tam zawrzeć?

# Hint: W razie problemów z cudzysłowami w XPATH pod Windows, możesz zamienić je na apostrofy, np.:
#     "//div[@id='wartosc']" 
# zamiast 
#     '//div[@id="wartosc"]'

import click
import requests
from lxml import html

@click.command()
@click.argument('url')
@click.argument('xpath')

def main(url, xpath):
    page = requests.get(url)
    content = page.text
    elements = get_elements(content, xpath)
    for element in elements:
        print(element)

def get_elements(site_url, xpath_value):
    """
    This program extracts selected information from selected websites.
    The user enters only the website address and the xpath path, which can be easily copied in the browser.
    """

    tree = html.fromstring(site_url)
    elements = tree.xpath(xpath_value)
    elements = [e.text_content().strip().replace("\n", " ") for e in elements]
    return elements

if __name__ == "__main__":
    main()

# python M05\M05L20_projekt.py https://www.kaufland.pl/oferta/aktualny-tydzien/przeglad.category=01_Mi%C4%99so__Dr%C3%B3b__W%C4%99dliny.html "//h4[@class='m-offer-tile__title']"
    

