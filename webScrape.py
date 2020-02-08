import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://theinternship.io'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"column is-one-third-desktop is-half-tablet"})

companyList = []
for container in containers:
   
    company = container.div.div.a.img['src']
    text = container.findAll("span", {"class": "list-company"})
    print(text)
    companyList.append(company)
companyList.sort(key = len)
for i in companyList:
    print("Company: " + i)


   