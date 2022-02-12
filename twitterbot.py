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
giris.send_keys("taehyuung2")
giris.send_keys(Keys.ENTER)

time.sleep(3)
sifre=driver.find_element_by_name("password")
sifre.send_keys("20052005Rny")
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









"""link="/taehyungrny/status/1488427147194781698"
driver.get("https://twitter.com"+link)
time.sleep(7)
driver.find_element_by_class_name('css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1p0dtai.r-xoduu5.r-1d2f490.r-xf4iuw.r-1ny4l3l.r-u8s1d.r-zchlnj.r-ipm5af.r-o7ynqc.r-6416eg').click()
time.sleep(2)
reply=driver.find_element_by_class_name('public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
reply.send_keys("I vote for #BTSARMY for the #BestFanArmy at the #iHeartAwards (@BTS_twt) 1")
time.sleep(2)
driver.find_element_by_class_name('css-18t94o4.css-1dbjc4n.r-l5o3uw r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr').click()
time.sleep(8)
tweet_url="https://twitter.com/taehyungrny/status/1488427147194781698"
driver.get(tweet_url)
time.sleep(4)
yanıt_click=driver.find_element_by_xpath('//*[@id="id__5n3uz9ddch9"]/div[1]/div/div/div/svg').click()
time.sleep(4)
yanıt_tweet=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
yanıt_tweet.send_keys("I vote for #BTSARMY for the #BestFanArmy at the #iHeartAwards (@BTS_twt) 1")"""




"""
profil_click=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div/div[2]/span').click()
time.sleep(4)
oy_tweet=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/article').click()
time.sleep(4)
yanıt=driver.find_element_by_xpath('//*[@id="id__om0qfvolcg"]/div[1]/div/div/div/div').click()"""
