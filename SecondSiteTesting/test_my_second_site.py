# ###############################################################################
# ###############################################################################
# ###############################################################################

# Starter essential code to get Selenium for Python running.

from selenium import webdriver          

chrome_browser = webdriver.Chrome('./chromedriver')

print(chrome_browser) 
# Output in the terminal is <selenium.webdriver.chrome.webdriver.WebDriver (session=" A BUNCH OF NUMBERS HERE ")>

# ###############################################################################
# ###############################################################################
# ###############################################################################

chrome_browser.maximize_window()
# What do you want Selenium to test?
chrome_browser.get('https://www.andrewzdunek.com/');

