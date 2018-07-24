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
BlacklistedLinks = ["facebook.com", "instagram.com", "twitter.com", "mailto", "utexas.edu", "hackreactor.com", "capitalfactory.com", "atxwomen.com", "bizjournals.com", "siliconhillsnews.com"]#used to remove links outside of website
#function
def getPageLinks(link):
    BlacklistedLinks.append(link)#add it so it doesnt call itself
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
    for BlackLink in BlacklistedLinks:#remove links already visited and ones that go off the site
        purelinks = [link for link in purelinks if BlackLink not in link]
    purelinks = [link for link in purelinks if "#" != link[0]]
    if "/" in purelinks: #remove any links that go nowhere
        purelinks.remove("/")
    fullLinks = []
    for link in purelinks:#add rest of link
        fullLinks.append("http://www.helloworldstudio.org" + link)
    time.sleep(0.1)
    return fullLinks

#code
graph = {"http://www.helloworldstudio.org/home" : getPageLinks("http://www.helloworldstudio.org/home")}#starting at home
for link in graph["http://www.helloworldstudio.org/home"]:
    graph[link]=getPageLinks(link)

#write graph to file
with open("data.json", "w") as data:
    data.write(json.dumps(graph))