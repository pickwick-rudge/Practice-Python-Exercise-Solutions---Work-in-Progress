#Coder: Michael Kich

'''Task: Use the BeautifulSoup and requests Python packages to print out a list
of all the article titles on the New York Times homepage.'''

#Import requests and the BeautifulSoup
import requests
from bs4 import BeautifulSoup

#Make url an independent variable, so that it's easier to swap out for a new url if desired
url = "https://www.nytimes.com/"

#Use the get function in the requests library to fetch the url and set it equal to the fetch variable
fetch = requests.get(url)

#Now, set the variable soup = to BeautifulSoup, with just the content, and also with the parser set to lxml
soup = BeautifulSoup(fetch.content, features="lxml")

#For every link on the page, find all that have the "span" tag, then print the link in a text format
for link in soup.find_all("span"):
    print(link.text)

for link in soup.find_all("h2"):
    print(link.text)
