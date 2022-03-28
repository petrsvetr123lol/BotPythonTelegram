from bs4 import BeautifulSoup
import requests
import time

commit1 = "zero"
commit2 = ""

while True:

    url = "https://github.com/petrsvetr123lol/Filip-Test-Vektory/commits"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    commit1 = doc.find(class_="Link--primary text-bold js-navigation-open markdown-title", href=True)

    print(commit1)
    if commit1 != commit2:
        requests.post(
            'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
            '=-604401103', data={
                'text': 'Commited in'
            }).json()
        requests.post(
            'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
            '=-604401103', data={
                'text': url,
            }).json()
        requests.post(
            'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
            '=-604401103', data={
                'text': commit1,
            }).json()
        commit2 = commit1
    else:
        requests.post(
            'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
            '=-604401103', data={
                'text': 'All commits were sent'
            }).json()
    time.sleep(1800)
