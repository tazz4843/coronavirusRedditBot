# Uses code from https://github.com/carlos-menezes/worldometers.py/blob/master/worldometers.py

from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

# Snippet of code that I might have to fall back to
"""
try:
    d = webdriver.Chrome()
except Exception as e:
    try:
        d = webdrive.Firefox()
    except Exception as e:
        print('No web browsers installed! Please install Mozilla Firefox or Google Chrome!')
d.get('https://www.worldometers.info/coronavirus/')
print(d.find_element_by_css_selector('[rel="maincounter-number"]').text)
"""
def getCases():
    url = 'https://www.worldometers.info/coronavirus/'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    return int(soup.find(id='maincounter-number').getText().replace(',', ''))

def getDeaths():
    url = 'https://www.worldometers.info/coronavirus/'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    return int(soup.find(id='maincounter-number').getText().replace(',', ''))
