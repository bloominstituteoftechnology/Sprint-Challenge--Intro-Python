import requests
import re

# get the data
data = requests.get('https://www.swfc.co.uk/club/club-contacts/')

# extract all emails on a web page
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print(emails)