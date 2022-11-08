import requests
from bs4 import BeautifulSoup

URL = "https://www.baseball-reference.com/friv/birthdays.cgi"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="div_birthday_stats")

def list_of_names():
    """
    Returns a list of names of players whose birthday is today
    """
    name_elements = results.find_all(class_="left", attrs={"data-stat": "player"})

    names = []
    for name_element in name_elements:
        names.append(name_element.text)
    names.pop(0) # the first element is always "Name", do not want that

    return names 