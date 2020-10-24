# This is about accessing different elements in a HTML Webpage. You can even search
# something on the webpage in the searchbar if you have to. First step is to
# right-click the thing you want to automate and select the option inspect.

from selenium import webdriver # importing webdriver from selenium
from selenium.webdriver.common.keys import Keys # importing keys like enter and backspace from selenium

while True: # Creating a loop to search continously
    a = input("What do you want to search on Google ? - "+'\n')

    if a:
        PATH = "C:\Program Files (x86)\msedgedriver.exe" # The path of the webdriver
        driver = webdriver.Edge(PATH) # Getting the path

        driver.get("https://www.google.com") # Getting the url **Please include "https://".**
        print('\n')
        
        search = driver.find_element_by_name("q") # In this, clicking on inspect in the google searchbar, I am inserting the name which is "q"
        search.send_keys(a) # This is what, I am going to type in the search bar of google
        search.send_keys(Keys.RETURN) # The "RETURN" is the key to press enter for automation

    else:
        break

