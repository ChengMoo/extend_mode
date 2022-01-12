import sys

if len(sys.argv) < 2:
    print('argv Error')
else:
    users = [sys.argv[1]]
    passwords = [sys.argv[2]]
    if " " in users[0] and " " in passwords[0]:
        users = users[0].split(" ")
        passwords = passwords[0].split(" ")

print(users, passwords)


import random
import time
import os
# import re
# import zipfile
# import requests
# import selenium
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import DesiredCapabilities
# import undetected_chromedriver as uc
from pyshadow.main import Shadow
from translate import Translator



class LanguageTrans():
    def __init__(self, mode):
        self.mode = mode
        if self.mode == "E2C":
            self.translator = Translator(from_lang="english", to_lang="chinese")
        if self.mode == "C2E":
            self.translator = Translator(from_lang="chinese", to_lang="english")
    def trans(self, word):
        translation = self.translator.translate(word)
        return translation




def load_driver(url):
    global driver
    try:
        driver.get(url)
        return driver
    except TimeoutException:
        time.sleep(5)
        driver.delete_all_cookies()
        try:
            driver.get(url)
            return driver
        except TimeoutException:
            print('timeout')
            return


def input_dependence():
    global driver, shadow
    # 启动浏览器内核
    opt = ChromeOptions()
    opt.headless = False
    path_e = os.getcwd() + r"\buster.crx"
    opt.add_extension(path_e)
#     path_e = os.getcwd() + r"\random-user-agent.crx"
#     opt.add_extension(path_e)
#     path_e = os.getcwd() + r"\canvas-fingerprint-blocker.crx"
    opt.add_extension(path_e)
#     opt.add_argument("window-size=1920,1080")
    opt.add_argument("--start-maximized")
    opt.add_argument('--no-sandbox')
    # 设置开发者模式启动，该模式下webdriver属性为正常值
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument('--disable-blink-features=AutomationControlled')
    ser = Service("chromedriver")
    driver = Chrome(service=ser, options=opt)
    # driver = uc.Chrome(browser_executable_path="chromedriver", options=opt, suppress_welcome=False, use_subprocess=True) # service=ser, options=opt
    shadow = Shadow(driver)
    driver.set_page_load_timeout(300)
    return driver

def change_seeting():
    global driver, shadow
    element = shadow.find_element("#devMode")
    element.click()
    time.sleep(3)
    element = shadow.find_element('#detailsButton')
    time.sleep(3)
    element.click()
    time.sleep(10)
    element = shadow.find_element('#host-access')
    element.click()
    # element.click()
    # element.send_keys(Keys.CONTROL + Keys.DOWN + Keys.DOWN + Keys.ENTER)
    all_options = element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        try:
            print(translator.trans("选项显示的文本 "), translator.trans(option.text))
            print(translator.trans("选项值为 "), translator.trans(option.get_attribute("value")))
        except:
            print(translator.trans("选项显示的文本 "), option.text)
            print(translator.trans("选项值为 "), option.get_attribute("value"))
    # WebDriverWait(option, 3, 0.1).until(EC.element_to_be_clickable((By.LINK_TEXT, '在所有网站上'))).click()
    time.sleep(2)
    option.click()
    element = shadow.find_element('#centeredContent')
    time.sleep(2)
    element.click()
    time.sleep(2)
    element = shadow.find_element('#closeButton')
    time.sleep(2)
    element.click()
    time.sleep(2)

def sign_in():
    global driver
    # 加载登陆界面
    load_driver("https://hax.co.id/login")
    time.sleep(60)
    # 输入登陆信息
    ID = users[0]
    password = passwords[0]
    driver.find_element(By.XPATH, '//*[@id="text"]').send_keys(ID)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(random.uniform(2, 5))
    # 点击验证
    driver.switch_to.frame(driver.find_element(By.XPATH,
                                               '/html/body/main/div/div/div[2]/div/div/div/div/div/form/div[3]/div/div/div/iframe'))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
    driver.switch_to.default_content()
    time.sleep(1)
    element = driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[10]/div[4]/iframe'))
    time.sleep(random.uniform(3, 5))
    driver.find_element(By.CSS_SELECTOR,
                        '#rc-imageselect > div.rc-footer > div.rc-controls > div.primary-controls > div.rc-buttons > div.button-holder.help-button-holder')
    Ac = ActionChains(driver)
    Ac.send_keys(Keys.TAB).perform()
    Ac.send_keys(Keys.ENTER).perform()
    print(translator.trans("点击了"))
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        'body > div > div > div.rc-footer > div.rc-controls > div.primary-controls > div.rc-buttons > div.button-holder.help-button-holder')
    Bc = ActionChains(driver)
    Bc.send_keys(Keys.TAB).perform()
    Bc.send_keys(Keys.ENTER).perform()
    time.sleep(5)
    print(1)



translator = LanguageTrans("C2E")
if __name__ == '__main__':
    input_dependence()
    translator = LanguageTrans("C2E")
    time.sleep(3)
    # 选项修改
    load_driver("chrome://extensions/")
    time.sleep(5)
    try:
        change_seeting()
    except:
        pass
    count = 0
    while True:
        print("Reload sign pages")
        try:
            sign_in()
            driver.switch_to.default_content()
            driver.switch_to.default_content()
            driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div/div/div/div/form/button').click()
            time.sleep(30)
        except: 
            pass
        time.sleep(random.uniform(10, 20))
        count += 1
        if count >= 10:
            exit(3)
        if driver.current_url == "https://hax.co.id/vps-info/":
            break

    print("login sucess")
    load_driver('https://hax.co.id/vps-renew/')
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="web_address"]').send_keys("hax.co.id")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        '/html/body/main/div/div/div[2]/div/div/div/div/div/form/fieldset/div/div/div/input').click()
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]').click()
        time.sleep(3)
    except:
        time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div/div/div/div/form/button').click()
    time.sleep(30)
    print("Renew OK!")
