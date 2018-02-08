# import Beautiful Soup to parse HTML
from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, "html.parser") # make it a BeautifulSoup object

print(soup.prettify) # use the prettify() method to get a nicely formatted Unicode string
