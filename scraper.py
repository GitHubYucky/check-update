import csv
import os
import sys
import requests

import slackweb
import pandas as pd
from bs4 import BeautifulSoup

def scraping():
    url = 'https://qiita.com/ryo-futebol/items/235c212fdfc3704b7e9c'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = []
    for top_news in soup.find_all(class_='取得したい箇所のクラス名'):
        result.append([
            top_news.text,
            top_news.get('href')
        ])
    return result

scraping()
