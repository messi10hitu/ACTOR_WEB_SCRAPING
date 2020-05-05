import requests
import urllib.request
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import pandas as pd
from urllib.request import urlopen
import re
import json
import csv

# to find only links
l6 = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# count = 0
html = urlopen("https://www.imdb.com/list/ls020280202/")
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('.jpg')})
for image in images:
    # count += 1
    # print(str(count))
    link = (str(image['src']) + '\n')
    l6.append(link)
print(str(l6))


# def dl_jpg(url, file_path, file_name):
#     full_path = file_path + file_name + ".jpg"
#     urllib.request.urlretrieve(url, full_path)
#
#
# url = "https://m.media-amazon.com/images/M/MV5BMjAwMjk3NDUzN15BMl5BanBnXkFtZTcwNjI4MTY0NA@@._V1_UX140_CR0,0,140," \
#       "209_AL_.jpg "
# file_name = input("enter file name to save as: ")
#
# dl_jpg(url,'/scrapped_images/',file_name)