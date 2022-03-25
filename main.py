from bs4 import BeautifulSoup
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
print(tag)
