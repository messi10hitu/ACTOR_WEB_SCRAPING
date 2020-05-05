import requests
# from bs4 import BeautifulSoup
# from io import BytesIO
# from PIL import Image
#
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
# #                   'Chrome/58.0.3029.110 Safari/537.3'}
# search = input("search for: ")
# params = {"q": search}
#
# url = "https://www.imdb.com/list/ls068010962/"
#
# # STEP 1. get the HTML.
# r = requests.get(url, params=params)
# # html_content = r.content
# # print(html_content)
#
# # STEP 2. Parse the HTML.
# soup = BeautifulSoup(r.text, "html.parser")
# links = soup.find_all("a")
#
# for item in links:
#     img_obj = requests.get(item.attrs["href"])
#     title = item.attrs["href"].split("/")
#     img = Image.open(BytesIO(img_obj.content))
#     img.save("/scrapped_images/" + title, img.format)


import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from PIL import Image
from string import ascii_lowercase

i = 1


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


soup = make_soup("https://www.imdb.com/list/ls020280202/")
for img in soup.findAll('img'):
    temp = img.get('src')
    if temp[:1] == "/":
        image = "https://www.imdb.com/list/ls020280202/" + temp
    else:
        image = temp

    print(image)

    nametemp = img.get('alt')
    if len(nametemp) == 0:
        filename = str(i)
        print(str(filename))
        i = i + 1
    else:
        filename = nametemp

    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()

# for f in os.listdir('C:\\Users\\hitesh\\PycharmProjects\\WebScrapping'):
#     if f.endswith('.jpeg'):
#         i = Image.open(f)
#         fn, fext = os.path.split(f)
#         i.save("scrapped_images.jpeg".format(fn))
