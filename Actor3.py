import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import json
import csv
import re
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
movies = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = "https://www.imdb.com/list/ls020280202/"

# STEP 1. get the HTML.
r = requests.get(url, headers=headers)
html_content = r.content
# print(html_content)

print("ACTORS NAME")
# # STEP 2. Parse the HTML.
soup = BeautifulSoup(html_content, "html.parser")
for item in soup.find_all("div",class_="lister-item-content"):
    for header in item.find_all("h3",class_="lister-item-header"):
        for anchor in header.find_all("a"):
        # print(anchor.text.strip())
            l1.append(anchor.text.strip())
print(l1)


print(" LINKS OF THE URLS")
# LINKS
html = urlopen("https://www.imdb.com/list/ls020280202/")
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('.jpg')})
for image in images:
    # count += 1
    # print(str(count))
    link = (str(image['src']) + '\n')
    l6.append(link)
# print(str(l6))


print(" ROLE: ")
# ACTORS
for item in soup.find_all("div",class_="lister-item-content"):
    for para in item.find_all("p",class_="text-muted text-small"):
        l2.append(para.text.strip())
        for anchor in para.find_all("a"):
            l3.append(anchor.text.strip())
# print(l2)
l2 = str(l2)
r = re.findall(r'Actor', l2)
print(r)
# print(l3)


print("DESCRIPTION" )
# DESCRIPTION
for item in soup.find_all("div",class_="lister-item-content"):
    for para in item.find_all("p"):
        l4.append(para.text.strip())
l4 = l4[1::2]
print(l4)


# TOP RATED MOVIES
# for div in soup.find_all("div",class_="lister-item mode-detail"):
for item in soup.find_all("div", class_="list-description"):
    for para in item.find_all("p"):
        print(para.text.strip())
        l5.append(para.text.strip())
l5 = l5
print(l5)
# data = str(l5)
# # print(type(data))
# print("MOVIES YEAR:")
# z = re.findall(r'\(\d{4}\)', data)
# print(z)
# 
# print("MOVIES RATINGS:")
# z = re.findall(r'\d.\d/\d+', data)
# print(z)
#
# print("MOVIES NAMES:")
# z = re.findall(r'\d\)\d \w+|\d\)\w+ \w+ \w+|\d\)\w+|\d\)\w+ \w+|\d\)\w+ \w+ \w+ \w+', data)
# print(z)


df1 = pd.DataFrame(r, columns=["ROLE"])  # dataframe is an excel sheet which we can use in the python
df1['ACTOR NAME'] = pd.DataFrame(l1)  # dataframe is an excel sheet which we can use in the python
df1['DETAILS'] = pd.DataFrame(l5)  # dataframe is an excel sheet which we can use in the python
df1['LINKS'] = pd.DataFrame(l6)
df1['DESCRIPTION'] = pd.DataFrame(l4)
print(df1)
df1.to_csv("A2.csv")