#imports
from bs4 import BeautifulSoup
import requests
import json
import time

#classes
class Link:
    def __init__(self, link):
        self.link = link
        self.children = []
#function
def getPageLinks(link):
    page = requests.get(link)#get page html
    soup = BeautifulSoup(page.text, "html.parser")#parse with soup
    links = soup.find_all("a")#remove all but a links
    purelinks=[]
    for link in links:
        purelinks.append(link.get("href"))#get the pure links
    #scrub out unusable links
    for link in purelinks:#remove and a tags with no links
        if link is None:
            purelinks.remove(None)
    purelinks = [link for link in purelinks if "http" not in link]
    purelinks = [link for link in purelinks if "#" != link[0]]
    if "/" in purelinks: #remove any links that go nowhere
        purelinks.remove("/")
    fullLinks = []
    for link in purelinks:#add rest of link
        fullLinks.append("http://www.helloworldstudio.org" + link)#change base on domain
    time.sleep(0.1)
    return fullLinks

#code
basePage = "http://www.helloworldstudio.org/home"
graph = {basePage : getPageLinks(basePage)}#starting at home
counter = 0
for link in graph[basePage]:
    counter+=1
    graph[link]=getPageLinks(link)
    if(counter>1000):
        break

#write graph to file
with open("data.json", "w") as data:
    data.write(json.dumps(graph))