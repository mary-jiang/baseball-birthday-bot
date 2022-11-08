import requests

URL = "https://www.baseball-reference.com/friv/birthdays.cgi"
page = requests.get(URL)

print(page.text)