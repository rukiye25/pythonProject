from dataclasses import replace
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



driver=webdriver.Chrome()
url="https://twitter.com/home"
driver.get(url)
time.sleep(3)
driver.maximize_window()
time.sleep(1)
giris=driver.find_element_by_name("text")
giris.send_keys("username")
giris.send_keys(Keys.ENTER)

time.sleep(3)
sifre=driver.find_element_by_name("password")
sifre.send_keys("password")
sifre.send_keys(Keys.ENTER)
time.sleep(4)

sayac=1
"""while sayac<51:
    tweei_click=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span').click()
    time.sleep(4)
    tweet=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    tweet.send_keys("I vote for #BTSARMY for the #BestFanArmy at the #iHeartAwards (@BTS_twt) {}".format(sayac))
    time.sleep(2)
    tweet_click=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()
    sayac+=1
    time.sleep(5)"""

while sayac<51:
    tweei_click=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span').click()
    time.sleep(4)
    tweet=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    tweet.send_keys("I vote for #BUTTER for the #BestMusicVideo at the #iHeartAwards (@BTS_twt) {}".format(sayac))
    time.sleep(2)
    tweet_click=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()
    sayac+=1
    time.sleep(5)








