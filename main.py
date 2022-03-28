from bs4 import BeautifulSoup, SoupStrainer
import requests
import urllib.request
import time

while True:
    url = "https://github.com/petrsvetr123lol/Filip-Test-Vektory/commits"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    commit = doc.find(class_="Link--primary text-bold js-navigation-open markdown-title", href=True)
    print(commit)

    requests.post(
        'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
        '=-604401103', data={
            'text': commit
        }).json()
