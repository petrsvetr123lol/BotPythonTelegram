from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3060-gv-n3060eagle-oc-12gd/p/N82E16814932434?Item=9SIAPBWFVW0978"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
