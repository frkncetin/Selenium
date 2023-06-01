from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.etiya.com")
driver.maximize_window()
sleep(2)


menuOpener = driver.find_element(By.ID, "nav-icon")
menuOpener.click()
sleep(2)


products = driver.find_element(By.XPATH, "//*[@id='menu-container']/ul/li[2]/a")
actionChain = ActionChains(driver)
actionChain.move_to_element(products).perform()
sleep(1)
productsItem = driver.find_element(By.XPATH, "//*[@id='scroll2']/ul/li[11]/a")
productsItem.click()
sleep(1)
cbBrochure = driver.find_element(By.XPATH, "//*[@id='page-block']/div[2]/div[2]/a[1]")
cbBrochure.click()
sleep(1)
submitButton = driver.find_element(By.XPATH, "//*[@id='download-br']/div[7]")
submitButton.click()
sleep(1)

for i in range(1,5):
    field = driver.find_element(By.XPATH, f"//*[@id='download-br']/div[{i}]/input")
    field.click()
    field.send_keys("Merhaba")
    sleep(1)

submitButton.click()

checkBox = driver.find_element(By.XPATH, "//*[@id='download-br']/div[5]/label")
checkBox.click()

submitButton.click()



sleep(30)







