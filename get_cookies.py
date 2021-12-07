import pickle
import time
from selenium import webdriver

#change your dir here
dir = '/usr/lib/chromium-browser/chromedriver'
browser = webdriver.Chrome(dir)

#the url after login
url = "https://glados.rocks/console/checkin"
#the final url before login, or the url needed login
last_url = "https://glados.rocks/console"

browser.get(last_url)
flag = True
while flag:
    print("Please login in!")
    time.sleep(2)
    while browser.current_url == url:
        browser.get("https://glados.rocks/console")
        pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
        browser.quit()
        flag = False

print("Cookies have successfully saved in cookies.pkl!")