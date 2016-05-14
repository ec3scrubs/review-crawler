import urllib
from bs4 import BeautifulSoup
import requests

upper, multiplier = 9, 20
url = 'https://www.yelp.com.sg/biz/tian-tian-hainanese-chicken-rice-singapore-2'
offset_url = '?start='

def main():
    global url, upper, multiplier
    full_url = ""
    for i in xrange(0, upper):
        if i == 0 :
            full_url = url
        else :
            full_url = url + offset_url + str(i * multiplier)
        r = requests.get(full_url)
        u = urllib.URLopener()
        try :
            u.retrieve(full_url, 'dl/'+str(i+1))
        except IOError :
            continue

if __name__ == "__main__":
    main()
