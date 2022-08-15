from getLinks import createSoup, nextPageAccess, pullLinks
import pandas as pd
import numpy as np

categories = ['news',
              'politics',
              'entertainment',
              'sports',
              'money',
              'business',
              'investing',
              'fashion',
              'beauty',
              'food',
              'recipes',
              'travel',
              'regional',
              'vacation',
              'health',
              'fitness',
              'home',
              'garden',
              'science',
              'technology',
              'cars',
              'hobbies',
              'lifestylemen',
              'lifestylewomen',
              'outdoors',
              'kids',
              'parenting']
news = []
politics = ['democrat', 'republican', 'liberal', 'conservative']
entertainment = ['celebrities', 'movies', 'music']
sports = ['running',	'golf',	'bicycling',	'mainstream',	'triatholon',	'tennis',	'soccer',	'sailing',
          'boxing',	'motorsports', 'Baseball', 'football', 'soccer', 'basketball', 'hockey', 'la+crosse', 'golf']
money = ['wealthy', 'people', 'entreapeneur']
business = ['companies',	'industries',	'marketing']
investing = ['venture+captial', 'private+equity', 'derivatives',
             'hedge+funds', 'public+markets', 'commodities', 'futures', 'options']
fashion = ['style',	'clothing',	'famous+people',	'trends']
beauty = [	'makeup',	'skincare',
           'fragrance',	'hair',	'beauty+products'	]
food = ['wine', 'recipes']
recipes = []
travel = ['summer',	'winter',	'fall',	'spring',	'cruising']
regional = ['midwest',	'country',	'southern',
            'coastal',	'cottage',	'international',	'canada',	'history']
vacation = []
health = ['mental',	'skin',	'men',
          'women',	'natural',	'diabetes', 'pregnacy']
fitness = []
home = ['architecture',	'style',
        'décor',	'housekeeping',	'handyman',	'DIY']
garden = ['projects',	'farming']
science = []
technology = ['mac',	'pc']
cars = ['cars',	'roads',	'racing',	'planes',	'sports']
hobbies = ['Woodworking',
           'Cooking',
           'BBQ',
           'Flying',
           'Climbing',
           'Sound',
           'Video+Games',
           'Musical+Instruments',
           'Photography',
           'Kayaking',
           'Scuba+diving',
           'Painting',
           'Writing',
           'Genealogy',
           'Shopping',
           'Drawing',
           'Sewing',
           'Photography',
           'Brewing',
           'Pottery',
           'Beekeeping',
           'Winemaking',
           'Learning',
           'Exercise',
           'Creative+writing',
           'Glass+blowing',
           'Singing',
           'Wood+Carving',
           'Chess',
           'Handicraft',
           'Metalworking',
           'Interior+Design',
           'Lotology',
           'Computer+Programing',
           'Video+Editing',
           'Hunting',
           'Soccer',
           'Marketing',
           'Digital+art',
           'Digial+Photography',
           '3D+printing',
           'Guitar',
           'Gymnastics',
           'Acting',
           'Lanaguages',
           'Film+making',
           'Archery',
           'Running',
           'Snowboarding',
           'Toy',
           'Knitting',
           'Carpenter',
           'Darts',
           'Roller+Skating',
           'Embroidery',
           'Hiking',
           'Base+Jumping',
           'Baseball',
           'Football',
           'Soccer',
           'Basketball',
           'Hockey',
           'La+crosse',
           'Golf']
lifestylemen = ['fashion',	'health']
lifestylewomen = ['self+help',	'fashion',	'adventure',	'culture']
outdoors = ['wildlife',	'camping',	'yachting',	'rock+climbing',
            'hiking',	'boating'	'fishing',	'hunting',	'mountain+biking']
kids = ['coloring',	'scouts',	'pets'	]
parenting = ['parenting',	'family']

all_categories = [
    news,
    politics,
    entertainment,
    sports,
    money,
    business,
    investing,
    fashion,
    beauty,
    food,
    recipes,
    travel,
    regional,
    vacation,
    health,
    fitness,
    home,
    garden,
    science,
    technology,
    cars,
    hobbies,
    lifestylemen,
    lifestylewomen,
    outdoors,
    kids,
    parenting]


def runScrape(category, text):
    for i in range(len(category)):
        searchTerm = text + '+' + category[i]
        url = ('https://www.google.com/search?q='+searchTerm)
        notWanted = ['youtube', 'google', 'search', 'wikipedia', 'dictionary']
        hotSoup = createSoup(url)
        array1Links = pullLinks(hotSoup, notWanted)
        nextPageLink = nextPageAccess(hotSoup)
        hotSoupPage2 = createSoup(nextPageLink)
        array2Links = pullLinks(hotSoupPage2, notWanted)
        arrLinks = np.concatenate((array1Links, array2Links))
        string_from_array = np.array2string(arrLinks)
        string_to_print = (searchTerm+': '+string_from_array)
        file = open('subCategories.txt', 'a')
        file.write(string_to_print+'\n')
    # file.close()


def runScrapeMain(category):
    for i in range(len(category)):
        searchTerm = category[i]
        url = ('https://www.google.com/search?q='+searchTerm)
        notWanted = ['youtube', 'google', 'search', 'wikipedia', 'dictionary']
        hotSoup = createSoup(url)
        array1Links = pullLinks(hotSoup, notWanted)
        nextPageLink = nextPageAccess(hotSoup)
        hotSoupPage2 = createSoup(nextPageLink)
        array2Links = pullLinks(hotSoupPage2, notWanted)
        arrLinks = np.concatenate((array1Links, array2Links))
        string_from_array = np.array2string(arrLinks)
        string_to_print = (searchTerm+': '+string_from_array)
        file = open('topCategories.txt', 'a')
        file.write(string_to_print+'\n')
    # file.close()


for j in range(len(all_categories)):
    category_text = categories[j]
    category_array = all_categories[j]
    runScrape(category_array, category_text)

runScrapeMain(categories)
