#Coder: Michael Kich

'''Use the BeautifulSoup and requests libraries to print off the full text of 
the article at this given website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture

The article is long, split between four pages.  The assigned task in the exercise is to 
print the entire text to the screen so that the user doesn't have to page through the article.
'''

#Import requests and the BS4 libraries
import requests
from bs4 import BeautifulSoup

#Create a url variable, to make swapping easier
url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

#Pass the url into the get() function with requests, and set equal to fetch - fetches the url
fetch = requests.get(url)

#Set soup variable = to BeautifulSoup, passing in the fetch arg and setting the parser to lxml
soup = BeautifulSoup(fetch.content, features="lxml")

#use find_all to find every word in html tags labeled "section", and print it
for word in soup.find_all("section"):
    print(word.text)


