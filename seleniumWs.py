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
menuItem = driver.find_element(By.XPATH, "//*[@id='menu-container']/ul/li[5]/a")
menuItem.click()
sleep(2)
categories = driver.find_element(By.CLASS_NAME, "blog-cat-h")
categories.click()
sleep(2)
catItem1 = driver.find_element(By.XPATH, "//*[@id='mCSB_1_container']/ul/li[1]")
catItem1.click()
sleep(2)
categories.click()
catItem2 = driver.find_element(By.XPATH, "//*[@id='mCSB_1_container']/ul/li[2]")
catItem2.click()
sleep(2)
#loadMore = driver.find_element(By.XPATH, "//*[@id='load-more']/span")

for _ in range(2):
    loadMore = driver.find_element(By.ID, "load-more")
    loadMore.click()
    sleep(3)

#loadMore2 = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[2]/div/div[13]")
#loadMore2.click()


#actionChain = ActionChains(driver)
#actionChain.move_to_element(loadMore)
#actionChain.click()
#actionChain.perform()




sleep(50)