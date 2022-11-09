import requests
import random
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

    return names[1:] # exclude header of table

def birthday_boy_stats():
    """
    Chooses a random MLB player whose birthday is the day the function is ran and returns a dictionary of that player's stats
    Please visit https://www.baseball-reference.com/friv/birthdays.cgi and highlight each column to learn more about what each stat means
    """
    birthday_boy_elements = results.find_all("tr")
    rows = birthday_boy_elements[1:] # exclude header of table

    chosen_row = random.choice(rows)
    stats = {}

    # fill in all the stats from baseball reference
    stats["name"] = chosen_row.find("td", attrs={"data-stat":"player"}).text
    stats["experience"] = int(chosen_row.find("td", attrs={"data-stat":"experience"}).text)
    stats["year_min"] = int(chosen_row.find("td", attrs={"data-stat":"year_min"}).text)
    stats["year_max"] = int(chosen_row.find("td", attrs={"data-stat":"year_max"}).text)
    stats["WAR"] = float(chosen_row.find("td", attrs={"data-stat":"WAR"}).text)
    stats["allstar_games"] = int(chosen_row.find("td", attrs={"data-stat":"allstar_games"}).text)
    stats["G"] = int(chosen_row.find("td", attrs={"data-stat":"G"}).text)
    stats["AB"] = int(chosen_row.find("td", attrs={"data-stat":"AB"}).text)
    stats["R"] = int(chosen_row.find("td", attrs={"data-stat":"R"}).text)
    stats["H"] = int(chosen_row.find("td", attrs={"data-stat":"H"}).text)
    stats["HR"] = int(chosen_row.find("td", attrs={"data-stat":"HR"}).text)
    stats["RBI"] = int(chosen_row.find("td", attrs={"data-stat":"RBI"}).text)
    stats["SB"] = int(chosen_row.find("td", attrs={"data-stat":"SB"}).text)
    stats["BB"] = int(chosen_row.find("td", attrs={"data-stat":"BB"}).text)
    stats["batting_avg"] = float(chosen_row.find("td", attrs={"data-stat":"batting_avg"}).text)
    stats["onbase_perc"] = float(chosen_row.find("td", attrs={"data-stat":"onbase_perc"}).text)
    stats["slugging_perc"] = float(chosen_row.find("td", attrs={"data-stat":"slugging_perc"}).text)
    stats["onbase_plus_slugging"] = float(chosen_row.find("td", attrs={"data-stat":"onbase_plus_slugging"}).text)
    stats["onbase_plus_slugging_plus"] = int(chosen_row.find("td", attrs={"data-stat":"onbase_plus_slugging_plus"}).text)
    stats["W"] = int(chosen_row.find("td", attrs={"data-stat":"W"}).text)
    stats["L"] = int(chosen_row.find("td", attrs={"data-stat":"L"}).text)
    stats["earned_run_avg"] = float(chosen_row.find("td", attrs={"data-stat":"earned_run_avg"}).text)
    stats["earned_run_avg_plus"] = int(chosen_row.find("td", attrs={"data-stat":"earned_run_avg_plus"}).text)
    stats["whip"] = float(chosen_row.find("td", attrs={"data-stat":"whip"}).text)
    stats["G_p"] = int(chosen_row.find("td", attrs={"data-stat":"G_p"}).text)
    stats["GS"] = int(chosen_row.find("td", attrs={"data-stat":"GS"}).text)
    stats["SV"] = int(chosen_row.find("td", attrs={"data-stat":"SV"}).text)
    stats["IP"] = float(chosen_row.find("td", attrs={"data-stat":"IP"}).text)
    stats["H_p"] = int(chosen_row.find("td", attrs={"data-stat":"H_p"}).text)
    stats["HR_p"] = int(chosen_row.find("td", attrs={"data-stat":"HR_p"}).text)
    stats["BB_p"] = int(chosen_row.find("td", attrs={"data-stat":"BB_p"}).text)
    stats["SO_p"] = int(chosen_row.find("td", attrs={"data-stat":"SO_p"}).text)
    stats["franchises"] = chosen_row.find("td", attrs={"data-stat":"franchises"}).text

    return stats