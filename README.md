# Python-Selenium-Google-Searcher
This repository contains python files which are mainly done using Selenium module.

This program is used to search on the google without opening google. This can be done using importing
a python module named "selenium". This module helps us to do browser automation and makes it more
easier to work with. There are also other modules named "pyautogui", which does tasks by literally
copying the mouse and keyboard movements. You just write and give the correct coordinates and done ! 
The software does it all. But in Selenium, they are copying the whole browser to do automation. 
Selenium can be used for web scraping which means we can interact with the elements in a HTML webpage.
Here we interacted with the element which was the google search bar. We wrote the code to click on the
search bar and type our input there and press enter to get the search results without opening google !



Selenium Documentation - https://selenium-python.readthedocs.io/

The Main requirements for this program are:

1 ) Install Python on your computer. Python can be installed from the main site and for this project
    I have used Python 3.8.5 version. Also make sure that you have pip installed on your computer.
    For any problems with pip, just go to https://pip.pypa.io/en/stable/installing/#id7 . To download
    python, go to https://www.python.org/downloads/ 

2 ) Install Selenium on your computer. It can be done using the "pip install selenium" in command prompt
    for windows users. For Mac or Linux, they have to do it using "sudo".

3 ) Webdriver installed on your computer. This can be done using the following steps :
    
    a ) First, go to your browser settings and select "About your browser". Just note down the version
        of your browser.

    b ) Next search in the net for "yourbrowsername webdriver". Go to the link for downloading the webdriver
        and download it accoording to your browser version. 

        If you are using Chrome, then go to - https://sites.google.com/a/chromium.org/chromedriver/downloads
        If you are using Edge, then go to - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    
    c ) After installing the webdriver, if you are windows user, go to the "Program Files (x86)" folder
        and paste the webdriver.exe file there. Normally it should work if we place the webdriver in any
        folder but in my case, it worked only when I moved that to the "Program Files (x86)" folder.
        If you are a Mac user or Linux, please make sure you have safely kept the webdriver.exe in an 
        important folder.
    
    d ) Now we are ready to do web automation. I have used Microsoft Edge Driver for this but you can 
        change the name of the "PATH" according to your browser.
