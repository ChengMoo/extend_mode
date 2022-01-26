#!/usr/bin/python
# -*-coding:utf-8-*-

# 作者仓库:https://github.com/spiritLHL/Gecko_sign
# 觉得不错麻烦点个star谢谢
# 活动页面 不可说，只能提供一个关键字ADS
# 适配Windows


import sys

if len(sys.argv) < 1:
    print('')
    sys.exit()
else:
    url = sys.argv[1]
    print("Your site: {}".format(url))

# url = "https://www.spiritlhl.top"
import random
import time
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from translate import Translator



def input_dependence():
    global driver, shadow
    # 启动浏览器内核
    opt = ChromeOptions()
    opt.headless = True
    # path_e = os.getcwd() + r"\buster.crx"
    # opt.add_extension(path_e)
    # path_e = os.getcwd() + r"\AutoVerify.crx"
    # opt.add_extension(path_e)
    opt.add_argument("window-size=1920,1080")
    # opt.add_experimental_option('prefs', prefs)  # 关掉浏览器左上角的通知提示
    # opt.add_argument("disable-infobars")  # 关闭'chrome正受到自动测试软件的控制'提示
    opt.add_argument('--no-sandbox')
    opt.add_argument("--disable-blink-features")
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument('--disable-gpu')
    opt.add_argument('--disable-dev-shm-usage')
    # opt.add_argument({"extensions.ui.developer_mode": True})
    # opt.add_experimental_option('useAutomationExtension', False)
    # opt.set_preference("extensions.firebug.allPagesActivation", "on")
    ser = Service("chromedriver")
    driver = Chrome(service=ser, options=opt)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"})
    # 加载影子模块
    # shadow = Shadow(driver)
    driver.set_page_load_timeout(300)


def main(url):
    print(1)
    driver.get(url)
    print(2)
    try:
        WebDriverWait(driver, 60, 1).until(EC.visibility_of_element_located((By.NAME, 'aswift_1')))
    except Exception as e:
        print(e)
        try:
            driver.get(url)
            WebDriverWait(driver, 60, 1).until(EC.visibility_of_element_located((By.NAME, 'aswift_1')))
        except Exception as e:
            print(e)
            driver.get(url)
    print(3)
    try:
        time.sleep(60)
        WebDriverWait(driver, 120, 1).until(EC.visibility_of_element_located((By.NAME, 'aswift_1')))
        driver.switch_to.frame(driver.find_element(By.NAME, 'aswift_1'))
        print(4)
        eles = driver.find_elements(By.TAG_NAME, 'a')
        list_urls = []
        list_site_urls = []
    except Exception as e:
        print(e)
        eles = driver.find_elements(By.TAG_NAME, 'a')
        list_urls = []
        list_site_urls = []
    status_r = random.uniform(0,10)
    if status_r <= 5:
    # if status_r > 5:
        # 回到初始页面，进行下一步操作
        # driver.switch_to.default_content()
        # eles = driver.find_elements(By.TAG_NAME, 'a')
        for i in eles:
            if 'google' not in i.get_attribute('href'):
                list_urls.append(i.get_attribute('href'))
    for i in eles:
        if 'double' in i.get_attribute('href') or 'googleadservices' in i.get_attribute('href') and status_r > 5:
            # continue
            list_urls.append(i.get_attribute('href'))
        elif url in i.get_attribute('href') and 'google' not in i.get_attribute('href'):
            list_site_urls.append(i.get_attribute('href'))
    # print(list_urls)
    print(5)
    list_urls = list(set(list_urls))
    list_urls = random.sample(list_urls, len(list_urls))
    if len(list_urls) > 10:
        list_urls = list_urls[0:10]
    list_site_urls = list(set(list_site_urls))
    list_site_urls = random.sample(list_site_urls, len(list_site_urls))
    print(5.6)
    if (len(list_urls) - len(list_site_urls)) > 1:
        for i in list_site_urls:
            list_site_urls.append(i)
    list_urls.extend(list_site_urls)
    list_urls = random.sample(list_urls, len(list_urls))
    print("clicked {} times".format(len(list_urls)))
    print(6)
    for j in list_urls:
        try:
            driver.get(j)
            print("clicked:")
            print(j)
        except Exception as e:
            print(e)
            continue
        time.sleep(random.uniform(60, 120))
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.uniform(60, 120))
        try:
            tp_url = driver.current_url
            cles = driver.find_elements(By.TAG_NAME, 'a')
            tp = []
            for k in cles:
                if tp_url in k.get_attribute('href') and 'http' in k.get_attribute('href') and 'google' not in k.get_attribute('href'):
                    tp.append(k.get_attribute('href'))
            if tp == []:
                tp.append(tp_url)
            elif len(tp) > 2:
                tp = tp[0:2]
            print(tp)
            for l in tp:
                try:
                    driver.get(l)
                    time.sleep(random.uniform(60, 120))
                except Exception as e:
                    print(e)
        except:
            pass
    print(7)
    try:
        driver.get(url)
        WebDriverWait(driver, 60, 1).until(EC.visibility_of_element_located((By.NAME, 'aswift_1')))
    except Exception as e:
        print(e)
        try:
            driver.get(url)
            WebDriverWait(driver, 60, 1).until(EC.visibility_of_element_located((By.NAME, 'aswift_1')))
        except Exception as e:
            print(e)
            driver.get(url)


def close_driver():
    global driver
    # 关闭浏览器内核
    try:
        driver.quit()
    except Exception as e:
        print(e)
        print("driver closed")
    print("closed")


if __name__ == '__main__':
    print("=================================================")
    print("start")
    # time.sleep(random.uniform(random.uniform(0, 500), 1000))
    input_dependence()
    count = 0
    try:
        main(url)
        print(count)
    except Exception as e:
        print(e)
        pass
    # time.sleep(random.uniform(160, 190))
    close_driver()
    print("closed end")
