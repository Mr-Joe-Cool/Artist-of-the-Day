from selenium import webdriver
import requests
import random
import re
import json
import wikipedia
from bs4 import BeautifulSoup

def scrape_img():
    # Generates random painter category URL from wikipedia
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "G", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letter = random.choice(alphabet)
    category_url = rf'https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_"{letter}"'
    print(category_url)

    
    # Converts webpage into soup
    html = requests.get(category_url)
    soup = BeautifulSoup(html.text, "html.parser")

    # Generates a list of html lines with wiki page links based on the painter letter category
    links = []
    for link in soup.find_all("a", attrs={"href" : re.compile(f"^/wiki/{letter}")}):
        if not "List of painters" in str(link) and not "wikipedia" in str(link) and not "accesskey" in str(link) and not "span" in str(link) and letter in str(link):
            links.append(link)
    raw_link = str(random.choice(links))

    # Trunkates chosen html line into a url
    match = re.search(r'href="([^"]+)"', raw_link)
    if match:
        wiki_url = "https://en.wikipedia.org" + match.group(1)
        print(wiki_url)

    # Path to save the screenshot
    screenshot_path = 'screenshot.png'

    # Configure the webdriver (assuming Chrome)
    PATH = "C:\\Users\\lance\\Desktop\\Programming\\Daily Image\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Open the webpage
    driver.get(wiki_url)

    # Capture screenshot of the entire webpage
    driver.save_screenshot(screenshot_path)

    # Quit the webdriver
    driver.quit()

def scrape():
    # Generates random painter category URL from wikipedia
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "G", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letter = random.choice(alphabet)
    category_url = rf'https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_"{letter}"'
    print(category_url)

    
    # Converts webpage into soup
    html = requests.get(category_url)
    soup = BeautifulSoup(html.text, "html.parser")

    # Generates a list of html with wiki page links based on the painter letter category
    links = []
    for link in soup.find_all("a", attrs={"href" : re.compile(f"^/wiki/{letter}")}):
        if not "List of painters" in str(link) and not "wikipedia" in str(link) and not "accesskey" in str(link) and not "span" in str(link) and letter in str(link):
            links.append(link)
    raw_link = str(random.choice(links))

    # Trunkates chosen html line into a url
    match = re.search(r'title="([^"]+)"', raw_link)
    if match:
        wiki_title = match.group(1)
    
    page = wikipedia.WikipediaPage(title=wiki_title)
    
    text = page.content
    
    return wiki_title, text
