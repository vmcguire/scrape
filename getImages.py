def pullImages(soup):
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    print(images)
