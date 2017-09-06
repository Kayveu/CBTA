from bs4 import BeautifulSoup as bsoup
import requests, os

os.system('cls')

url = "http://publicinterestlegal.org/county-list/"
response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

parsed = bsoup(response.content, "lxml")

complete = []

for i in parsed.find_all("tr"):
    store = []
    for k in i:
        store.append(k.get_text())

    complete.append(store)

print "Username: efung"
print "Size of complete list: %i" % len(complete)
print complete
