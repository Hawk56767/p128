from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
scraped_data = []
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
temp_list=[]

def scrape():
    bright_star_table=soup.find_all("table", attrs={"class": "wikitable sortable"})
    total_table=len(bright_star_table)
 
    table_body=table_body[1].find_all('td')
    for row in table_body:
        table_cols=row.find_all('td')
        print(table_cols)
        data = [i.text.rstrip() for i in table_cols]
        temp_list.append(data)
   
Star_names=[]
Distance=[]
Mass=[]
Radius=[]

stars_data=[]
for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    required_data=[Star_names,Distance,Mass,Radius]
    stars_data.append(required_data)
headers=['Star_name','Distance','Mass','Radius']
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv('scraped_data.csv',index=True,index_label="id")

