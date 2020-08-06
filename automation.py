# ###############################################################################
# ###############################################################################
# ###############################################################################

# Starter essential code to get Selenium for Python running.

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
show_message_button = chrome_browser.find_element_by_class_name("btn-default")
# this print is not needed for lines 52 through 57
# print(show_message_button.get_attribute('innerHTML'))

# ---------------------------------------------------------------

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()

user_message.send_keys('I AM EXTRA COOOOL')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I AM EXTRA COOOOL' in output_message.text

# There are so many Chrome windows how do we close 

# chrome_browser.quit()