import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import Main_page
from pages.televizory_page import Televizory_page
from pages.tv_and_kino_page import Tv_and_kino_page


def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "none"
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    g = Service('C:\\Users\\baldy\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g,)

    print("Start Test 1")


    mp = Main_page(driver)
    mp.select_tv_and_kino()

    tvkino = Tv_and_kino_page(driver)
    tvkino.select_tv()

    televizory = Televizory_page(driver)
    televizory.select_smart_tv()




