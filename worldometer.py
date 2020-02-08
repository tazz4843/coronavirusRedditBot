import pandas as pd

def getPage():
    try:
        country_table = pd.read_html('https://www.worldometers.info/coronavirus')[0]
    except urllib.error.URLError as e:
        country_table = getPage()
    return country_table

def getCases():
    country_table = getPage()
    num = 0
    for item in country_table['Total Cases'][:]:
        num = item + num
    return num

def getRecovered():
    country_table = getPage()
    num = 0
    for item in country_table['Total Recovered'][:]:
        num = item + num
    return num

def getCritical():
    country_table = getPage()
    num = 0
    for item in country_table['Total Critical'][:]:
        num = item + num
    return num

def getDeaths():
    country_table = getPage()
    num = 0
    for item in country_table['Total Deaths'][:]:
        num = item + num
    return num
