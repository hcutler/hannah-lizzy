import urllib2
import time
from bs4 import BeautifulSoup
from yaml import load, Loader


#get contents of CDS-NYU page
# URL = "http://cds.nyu.edu/people/"
# html_doc = urllib2.urlopen(URL).read()
# # soup = BeautifulSoup(html_doc)

# #save copy of HTML contents locally
# with open("cds-nyu.html", "w") as html_file:
#     html_file.write(html_doc)

with open("startups.html", "r") as html_file:
    local_html = html_file.read()

soup = BeautifulSoup(local_html)

contents = soup.find_all('a')
# print contents


# comps = []

for item in contents:
    name = item.text
    print name
    # comps.append({'name': name})

# for c in comps:
#     print c