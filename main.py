from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(filename="bot.log", level=logging.INFO)
commit1 = "zero"
commit2 = ""
github_url = ""
print("Bot is running!")
while True:

    ###our github repository
    url = "https://github.com/petrsvetr123lol/Filip-Test-Vektory/commits"

    ###beautiful soup stuff
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    ###finding latest commit - web scrapping
    links = []
    for link in doc.find_all('a', class_="Link--primary text-bold js-navigation-open markdown-title", href=True):
        links.append(link['href'])
        commit1 = links[0]
        github_url = "https://github.com" + commit1

    ###if - commit was not sent...
    if commit1 != commit2:

        requests.post(
            'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
            '=-604401103', data={
                'text': github_url,
            }).json()
        commit2 = commit1
        logging.info("Commit has been sent to the chat")
    ###else - commit was sent
    """
    else:
        requests.post(
            'https://api.telegram.org/bot5112690824:AAEwjrjQAxJtaWwyFDUa10pzltRBOAOqwS4/sendMessage?chat_id'
            '=-604401103', data={
                'text': 'All commits were sent'
            }).json()
    ###refresh eveery x seconds - default = 1800s
    time.sleep(30)
"""