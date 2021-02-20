#bu mödül ile selenium.webdriver.common.keys import Keys tuşları aktif ederiz
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
url="http://github.com"
driver.get(url)
driver.maximize_window()
searchInput=driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
#burada enter tuşuna basmasını yazmış bulunduk
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# css ile arama yaparken her boşluk girdiğimiz etiketin altındaki etikette ara demek oluyor
result=driver.page_source
print(result)
"""repo=driver.find_elements_by_css_selector(".repo-list-item a")
count=1
for i in repo:
    print(count,i.text)
    count+=1"""
driver.close()
