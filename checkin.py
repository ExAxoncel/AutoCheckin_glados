import schedule
import random
import time
import pickle
from selenium import webdriver


def checkin():
    
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')    #replace your chromedriver dir here

    browser.get('https://glados.rocks')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
            browser.add_cookie(cookie)
    browser.get('https://glados.rocks')     #refresh

    browser.get('https://glados.rocks/console/checkin')

    #click checkin button
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[2]/button').click()

    #copy the result
    time.sleep(2)
    result_msg = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div/div').text

    browser.quit()
    print(result_msg)

    
while True:
    checkin()
    schedule.every(1).days.do(checkin)
    time.sleep(random.randint(1,9) * 60 + random.randint(0,59))
