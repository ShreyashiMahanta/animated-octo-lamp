from bs4 import BeautifulSoup 
import csv
import time
from selenium import webdriver
import pandas as pd
import requests

#Url of the website
stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(stars_url)
print(page)

browsers = webdriver.Chrome("./chromedriver")
browsers.get(stars_url)

soup = BeautifulSoup(browser.page_source,"html.parser")
table = soup.find_all('table')
print(len(table))

#An array containing the headers
headers = ["Star_name","Distance","Mass","Radius"]

temp_list= []
table_rows = table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)


Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])



#def letsScrapData():

copy = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns= headers)
print(df2)

df2.to_csv('scraping.csv')

 # with open("scraping.csv", "w") as f:
  #  csvWriter = csv.writer(f)
   # csvWriter.writerow(headers)
    #csvWriter.writerows(final_planet_data)

