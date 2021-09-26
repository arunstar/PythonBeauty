
from bs4 import BeautifulSoup
import requests

r = requests.get("https://liquipedia.net/pubg/Portal:Players/South_Asia")
data = r.text

soup = BeautifulSoup(data,'html.parser')
for link in soup.find_all('a'):
    print(link)