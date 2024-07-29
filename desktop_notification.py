import requests
import xml.etree.ElementTree as ET
RSS_FEED_URL = "__link__"

def load_site():
    respond = requests.get(RSS_FEED_URL)
    return respond.content

def parseXML (rss):
    root = ET.fromstring(rss)
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}

        for child in item:

            if child.tag == '{https://www.google.com/search?q=google&rlz=1C1KNTJ_enNP1065NP1066&oq=google&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTISCAEQLhhDGMcBGNEDGIAEGIoFMg4IAhBFGCcYOxiABBiKBTIGCAMQRRhBMgYIBBBFGDwyBggFEEUYQTIGCAYQRRg8MgYIBxBFGDzSAQg1MTc3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8}content':
                news['media'] = child.attrib['url']
            else: 
                news[child.tag] = child.text.encode('utf8') 
        newsitems.append(news) 
def topStories(): 

    rss = load_site() 

    newsitems = parseXML(rss) 
    return newsitems 




