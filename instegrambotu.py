from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
url="https://www.instagram.com/"
driver.get(url)
driver.maximize_window()
giris=driver.find_element_by_name("username")
giris.send_keys("rukiss_5")
time.sleep(1)
sifre=driver.find_element_by_name("password")
sifre.send_keys("20052005Rny")
enter=driver.find_element_by_class_name("Igw0E.IwRSH.eGOV_._4EzTm").click()
