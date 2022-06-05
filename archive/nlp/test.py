import webbrowser
import time
from googlesearch import *
import requests


def scrape(phrase):
    flag = 0
    ext = "https://www.google.com/search?q="
    links = search(phrase, num=5, stop=5, pause=2)
    msg = phrase.replace(" ", "+")
    url = ext + msg
    i = 0
    for link in links:
        i += 1
        if 'wikipedia' in link:
            flag = 1
            l = link
            break

    if flag == 1:
        wiki = requests.get(l)

        wiki_c = wiki.content
        soup = BeautifulSoup(wiki_c, 'html.parser')
        data = soup.find_all('p')
        print("From Wikipedia: ")

        print(data[0].get_text())

        print(data[1].get_text())
        print(data[2].get_text())
        print(data[3].get_text())

    else:
        print("Wikipedia not available")
    print("Providing search results")
    webbrowser.open(url, new=1)
    time.sleep(3)


scrape("What is internet")