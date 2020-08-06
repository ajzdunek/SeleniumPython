# ###############################################################################
# ###############################################################################
# ###############################################################################

# Starter essentials to get Selenium for Python running.

from selenium import webdriver          

chrome_browser = webdriver.Chrome('./chromedriver')

# print(chrome_browser)

# ###############################################################################
# ###############################################################################
# ###############################################################################

chrome_browser.maximize_window()
# What do you want Selenium to test?
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# ---------------------------------------------------------------

# Will print out True 
# print('Selenium Easy Demo' in chrome_browser.title)

#Lets modify the title - now will print out False
# print('Selenium Easy Spaghetti Demo' in chrome_browser.title)

# ---------------------------------------------------------------

#We could keep using print or we could also use assert to see if someting exists. If it is false it will error out in the terminal/exit you out of the program.
# assert('Selenium Easy Spaghetti Demo' in chrome_browser.title)

# ---------------------------------------------------------------

# Example of getting an element :D 

# assert 'Selenium Easy Demo' in chrome_browser.title
# button = chrome_browser.find_element_by_class_name("btn-default")
#print(button)

# Inspecting the button's HTML
assert 'Selenium Easy Demo' in chrome_browser.title
button_text = chrome_browser.find_element_by_class_name("btn-default")
print(button_text.get_attribute('innerHTML'))

# ---------------------------------------------------------------

# assert 'Show Message' in chrome_browser.page_source