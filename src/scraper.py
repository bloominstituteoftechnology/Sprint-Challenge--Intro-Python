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


print(scrape_emails("https://www.swfc.co.uk/club/club-contacts/"))

soup = bs_scrape("https://www.swfc.co.uk/club/club-contacts/")

# grab the tags and print them
for item in soup.find_all("a"):
    print(item)
