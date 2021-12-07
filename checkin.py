import datetime
import time
import pickle
from selenium import webdriver

#browser = webdriver.Chrome('/Users/axon/Downloads/chromedriver')        #myMac
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')   #raspi


browser.get('https://glados.rocks')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get('https://glados.rocks')     #refresh

browser.get('https://glados.rocks/console/checkin')

#click checkin button
time.sleep(2)
browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/button').click()

#copy result
time.sleep(2)
result_msg = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div/div').text

browser.quit()
print(result_msg)