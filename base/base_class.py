import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):       # Получаем текущую URL
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):       # Производим сравнение слов
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method screenshot"""

    def get_screenshot(self):       # Делаем скриншот
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\baldy\\AquaProjects\\Elex\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):       # Производим сравнение URL
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method enter cart"""

    def enter_cart(self):
        cart = "//a[@class='header__cart']"
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, cart))).click()
        print("Enter cart")

    """Method assert final price"""

    def assert_final_price(self):
        cart_price = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cartPage__itemPriceNow item_price']"))).text.replace(' ', '')       # Цена товара в коризне
        final_price = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'cartPage__asidePriceTotal']"))).text.replace(' ', '')       # Итоговая цена
        assert cart_price == final_price
        print("Good value final price")

    """Method assert final price"""

