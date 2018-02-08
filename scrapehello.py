# import the python module: Beautiful Soup to parse HTML
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
all_goodbye_elements = soup.find_all(class_="goodbye") # "class" is a researved word in python, so we neeed an underscore here

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

print(type(all_list_items[0]))
print("----------")

print("All list items:")
for li in all_list_items:
  print(li.string)
print("----------")

print("Children of hello-list:")
for child in all_hello_elements[0].children:
  print(child.string)
print("----------")

print("List items within the hello tag:")
hello_list_items = all_hello_elements[0].find_all("li")
print (hello_list_items)
print("----------")

print("The hello-list element:")
the_hello_element = soup.find(id="hello-list")
print(the_hello_element)
print("----------")

img_tag = soup.find("img")
print("The img source:")
print(img_tag["src"])
print("----------")

# print out the elements of the “goodbye” list
print("The goodbye element:")
the_goodbye_element = soup.find(id="goodbye-list").find_all("li")
for ele in the_goodbye_element:
    print(ele.string)
print("----------")

# print out the width of the img element.
print("The width of the img element:")
img_tag = soup.find("img")
print(img_tag["width"])
print("----------")

# print out the URL that the <a> tag points to.
print("The URL:")
url = soup.find("a")
print(url["href"])
print("----------")
