import pyperclip
from selenium import webdriver
import sys
import time


def try_auto_enter_password(url, pas):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
    browser.get(url)
    time.sleep(10)
    browser.find_element_by_xpath("//input[@type='password']").send_keys(pas)
    print("success")
    time.sleep(5)
    browser.quit()
    sys.exit()


def copy_to_clipboard(x):
    pyperclip.copy(x)

