from itertools import count
from re import A, sub
import requests
import sys
import webbrowser
import bs4
import operator
import urllib
import pandas as pd

endings = ['.com/', '.edu/', '.gov/', '.org/']


def createSoup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return soup


def nextPageAccess(soup):
    for nextPage in soup.select('a[aria-label]'):
        nextPageLink = ('https://www.google.com' + nextPage.get('href'))
        return nextPageLink


def removeEndings(separator, text):
    for i in range(len(separator)):
        sep = separator[i]
        if operator.contains(text, sep):
            stripped = text.split(sep, 1)[0]
            completed = stripped+separator[i]
            return completed


def pullLinks(soup, removals):
    linkElements = soup.select('div#main > div > div > div > a')
    linkToPrint = len(linkElements)
    sub_str = removals
    for i in range(linkToPrint):
        link = linkElements[i].get('href')
        z = 0
        for x in sub_str:
            if operator.contains(link, x):
                z = z + 1
            else:
                z = z
        if z == 0:
            linkStripped = link.lstrip("/url?q=")
            print(removeEndings(endings, linkStripped))
            # webbrowser.open('https://www.google.com'+link)
