# adaugare librarii necesare
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializare browser chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizare fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')


# selector by ID

# selector by  Link Text

# selector by Partial Link Text

# selector by Name



# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Andy')

sleep(3)
chrome.quit()
