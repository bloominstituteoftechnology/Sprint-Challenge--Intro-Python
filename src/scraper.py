import requests
import re
from bs4 import BeautifulSoup


def scrape_emails(ADDR):
    # get the data
    data = requests.get(ADDR)
    # extract all emails on a web page
    emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

    return emails


def bs_scrape(ADDR):
    data = requests.get(ADDR)
    soup = BeautifulSoup(data.text, "html.parser")
    return soup


# print(scrape_emails("https://www.swfc.co.uk/club/club-contacts/"))

soup = bs_scrape("https://www.swfc.co.uk/club/club-contacts/")

# grab the tags and print them
#for item in soup.find_all("a"):
#    print(item)

# lets scrape the data from a game leaderboard now

umg = bs_scrape("https://umggaming.com/leaderboards")

leader = umg.find("table", {"id": "leaderboard-table"})

tbody = leader.find("tbody")

players = []

for tr in tbody.find_all("tr"):
    place = tr.find_all("td")[0].text.strip()
    username = tr.find_all("td")[1].text.strip()
    xp = tr.find_all("td")[3].text.strip()
    # print(place, username, xp)
    players.append({"place": place, "username": username, "xp": xp})

print(players)
