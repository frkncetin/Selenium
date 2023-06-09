#selenium.py isimlendirmesi yapma
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
#full-path url
driver.get("https://www.etiya.com")
sleep(5)
driver.maximize_window()

#defensive test
# workshop görevi => bu kısmı fonksiyon haline getir.
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "lang-select")))
languageSelector = driver.find_element(By.CLASS_NAME, "lang-select")
sleep(5)
languageSelector.click()
sleep(5)
turkishLanguage = driver.find_element(By.XPATH, "//*[@id='etiya']/header/div/div[2]/div[1]/div[2]/div[1]/a")
sleep(5)
turkishLanguage.click()
sleep(5)
searchBtn = driver.find_element(By.ID, "search-btn")
sleep(5)
searchBtn.click()

searchInput = driver.find_element(By.ID, "search-input")
searchInput.send_keys("merhaba")

searchIcon = driver.find_element(By.XPATH, "//*[@id='search-box']/form/div/button")
searchIcon.click()


## ActionChains
driver.get("https://www.etiya.com")
button = driver.find_element(By.XPATH,"//*[@id='home-leadform']/div[1]/div[1]/span[4]")
actionChain = ActionChains(driver)
actionChain.move_to_element(button)
actionChain.click()
actionChain.perform()
##
sleep(5000)

#3 tane testcase yazıp testlerini kodla
# menü testi

# menü testi bitiş