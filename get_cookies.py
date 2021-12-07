import pickle
import time

from selenium import webdriver

brower = webdriver.Chrome('/Users/axon/Downloads/chromedriver')         #myMac
#brower = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')    #raspi

#登录跳转后url
url = "https://glados.rocks/console/checkin"
#最后一步url
last_url = "https://glados.rocks/console"

brower.get(last_url)
flag = True
while flag:
    print("Please login in!")
    time.sleep(10)
    while brower.current_url == url:
        brower.get("https://glados.rocks/console")
        pickle.dump(brower.get_cookies() , open("cookies.pkl","wb"))
        brower.quit()
        flag = False

print("Cookies saved in Cookies.pickle!")