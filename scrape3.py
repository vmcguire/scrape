from itertools import count
from re import A, sub
from scrape import createSoup, nextPageAccess, pullLinks
import requests
import sys
import webbrowser
import bs4
import operator
import urllib
import pandas as pd


searchTerm = 'kauai'

url = ('https://www.google.com/search?q='+searchTerm)

notWanted = ['youtube', 'google', 'search', 'wikipedia', 'dictionary']

# endings = ['.com/', '.edu/', '.gov/', '.org/']

hotSoup = createSoup(url)

pullLinks(hotSoup, notWanted)

nextPageLink = nextPageAccess(hotSoup)

hotSoupPage2 = createSoup(nextPageLink)

pullLinks(hotSoupPage2, notWanted)

# nextPageLink2 = nextPageAccess(hotSoupPage2)
