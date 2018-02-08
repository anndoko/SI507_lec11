# import Beautiful Soup to parse HTML
from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, "html.parser") # make it a BeautifulSoup object

#print(soup.prettify) # use the prettify() method to get a nicely formatted Unicode string



# look up elements of the page
## searching by tag
all_list_items = soup.find_all("li")
all_divs = soup.find_all("div")

## searching by class
all_goodbye_elements = soup.find_all(class_="goodbye")

## searching by tag AND class
all_french_list_items = soup.find_all("li", class_="french")

## searching by id
all_hello_elements = soup.find_all(id="hello-list")

print("list items:\n", all_list_items)
print("----------")
print("div items:\n", all_divs)
print("----------")
print("hello id elements:\n", all_hello_elements)
print("----------")
print("goodbye elements:\n", all_goodbye_elements)
print("----------")
print("french stuff:\n", all_french_list_items)
