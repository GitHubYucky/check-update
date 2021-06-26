import csv
import os
import sys
import requests

import slackweb
import pandas as pd
from bs4 import BeautifulSoup

def scraping():
    url = 'https://news.yahoo.co.jp/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = []
    for top_news in soup.find_all(class_='sc-hmzhuo hkqpwM'):
        result.append([
            top_news.text,
            top_news.get('href')
        ])
    return result

def output_csv(result):
  with open('last_log.csv','w',newline='',encoding='utf_8') as file:
    headers=['Title','URL']
    writer=csv.writer(file)
    writer.writerow(headers)

def read_csv():
    if not os.path.exists('last_log.csv'):
        raise Exception('ファイルがありません。')
    if os.path.getsize('last_log.csv') == 0:
        raise Exception('ファイルの中身が空です。')
    csv_list = pd.read_csv('last_log.csv', header=None).values.tolist()
    return csv_list

result=scraping()
output_csv(result)
