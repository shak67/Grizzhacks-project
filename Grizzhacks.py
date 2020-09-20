import requests
from bs4 import BeautifulSoup

players = []

def bballScraper(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    # Players
    for element in soup.find('table').findAll('tr',{'class':'full_table'}):
        name = element.find('td',{'data-stat':'player'}).get_text()
        fg_pct = element.find('td',{'data-stat':'fg_pct'}).get_text()
        players.append({
             "name": name,
             "fg_pct": fg_pct

             })


url = '''https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'''
bballScraper(url)
print("Enter player name:")
user_input = input()
for d in players:
    if user_input == d['name']:
        print("found")
        print (d['name'] + " FG %: " + d['fg_pct'])
