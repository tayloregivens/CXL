import http.client, urllib.request, urllib.parse, urllib.error, base64, requests


# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
#this seems like it's scraping google scolar
#formats and prints out 2 pages of results, which is 20 results total bc 10 results per page
for i in range(0, 20, 10):
    url = "https://scholar.google.com/scholar?start=" + str(i) + '&q="primate"+AND+"threat"+AND+"conservation"&hl=en&as_sdt=0,5'
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')
    for item in soup.select('[data-lid]'):
        try: 
            print(item.select('.gs_rs')[0].get_text())
            print('----------------------------------------')
        except Exception as e:
            print('')