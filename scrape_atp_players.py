from bs4 import BeautifulSoup
import requests
import unidecode



URL = "https://live-tennis.eu/en/atp-live-ranking"
def get_players():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')



    results = soup.find_all('td',class_='pn')

    players = []
    for result in results[:100]:
        player_name = unidecode.unidecode(result.text)
        players.append(player_name)


    return players





