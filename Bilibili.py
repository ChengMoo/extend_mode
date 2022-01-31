#!/usr/bin/python
# -*-coding:utf-8-*-


import sys
import random
import time
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests




def input_dependence(status):
    global driver, shadow
    # 启动浏览器内核
    opt = ChromeOptions()
    opt.headless = status
    opt.add_argument("window-size=1920,1080")
    opt.add_argument('--no-sandbox')
    opt.add_argument("--disable-blink-features")
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument('--disable-gpu')
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--ignore-certificate-errors-spki-list')
    opt.add_argument('--ignore-ssl-errors')
    ser = Service("chromedriver")
    driver = Chrome(service=ser, options=opt)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"})
    driver.set_page_load_timeout(300)


def main(url):
    input_dependence(False)
    print(1)
    driver.get(url)
    times_list = []
    for i in range(0, 15):
        try:
            WebDriverWait(driver, 1, 0.1).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[11]/div[2]/div[2]/div[1]/div[2]/div')))
            page_text = driver.find_element(By.XPATH,
                                            '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[11]/div[2]/div[2]/div[1]/div[2]/div').text
            times_list.append(page_text)
        except:
            pass
        time.sleep(0.3)
    print(times_list)
    time_real = []
    for i in times_list:
        try:
            time_real.append(i.split(" / ")[-1])
        except:
            pass
    wait = 0
    for i in time_real:
        try:
            c = i.split(":")
            if c[0] == "00":
                continue
            cc = int(c[0]) * 60 + int(c[-1]) - int(random.uniform(10, 15))
            if cc > wait:
                wait = cc
        except:
            continue
    if wait == 0:
        wait = int(random.uniform(30, 60))
    print(f'wait {wait} scondes')
    time.sleep(wait)
    time.sleep(random.uniform(1, 6))
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(random.uniform(1, 6))


def close_driver():
    global driver
    # 关闭浏览器内核
    try:
        driver.quit()
    except:
        pass

def load():
    try:
        rr = requests.get("https://raw.githubusercontent.com/spiritLHL/extend_mode/main/Bilibili_sites.txt").text
    except:
        try:
            rr = requests.get("https://1.lvye.workers.dev/spiritLHL/extend_mode/raw/main/Bilibili_sites.txt").text
        except:
            rr = requests.get(
                "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/extend_mode/main/Bilibili_sites.txt").text
    real_sites = rr.split("\n")
    try:
        urls = [i for i in real_sites if (len(str(i)) != 0)]
        print("sites: \n{}".format(urls))
    except Exception as e:
        print(e)
        print("NO SETTING! \nPlease call spiritlhl!")
        sys.exit()
    print("=================================================")
    print("wait for start")
    print("start")
    try:
        rr = requests.get("https://raw.githubusercontent.com/spiritLHL/extend_mode/main/Bilibili_sites_status.txt").text
    except:
        try:
            rr = requests.get("https://1.lvye.workers.dev/spiritLHL/extend_mode/raw/main/Bilibili_sites_status.txt").text
        except:
            rr = requests.get(
                "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/extend_mode/main/Bilibili_sites_status.txt").text
    status_sites = int(rr)
    print(f"reload {str(status_sites)} times")
    if status_sites == 0:
        return
    temp = []
    for i in range(status_sites):
        for j in urls:
            temp.append(j)
    urls = temp.copy()
    random.shuffle(urls)
    print(urls)
    for url in urls:
        main(url)
    close_driver()
    print("closed end")

if __name__ == '__main__':
    load()
