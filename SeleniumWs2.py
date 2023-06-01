from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.etiya.com")
driver.maximize_window()
sleep(5)


newsLetter = driver.find_element(By.ID,"newsletter-form")
actionChain = ActionChains(driver)
actionChain.move_to_element(newsLetter)

#inputMail = driver.find_element(By.XPATH,"//*[@id='nval']")
sendButton = driver.find_element(By.ID,"send-newsl")
sendButton.click()
sleep(5)
closeButton = driver.find_element(By.CLASS_NAME,"swal-button-container")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal-button-container")))
closeButton.click()
sleep(5)

checkBox = driver.find_element(By.XPATH, "//*[@id='newsletter-form']/div[3]/label/ins")
checkBox.click()
sleep(3)
sendButton.click()
sleep(3)
closeButton.click()
actionChain.perform()

sleep(50)