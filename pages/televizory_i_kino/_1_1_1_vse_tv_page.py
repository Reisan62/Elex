import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Vse_tv_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    brend_spisok = "//span[.='Бренд']"       # Список брендов
    vybor_brenda = "//span[.='SAMSUNG ']"       # Выбираем бренд ( в данном случаей SAMSUNG)
    smart_spisok = "//span[.='Smart TV']"       # Список Smart TV
    vybor_smart_tv = "//label[@for='arrFilter_17_1004570158']//span[.='есть ']"       # Выбор наличиня Smart TV ( в данном случаей "есть")
    razreshenie_ekrana_spisok = "//span[.='Разрешение экрана']"       # Список разрешений экрана
    vybor_razreshenie_ekrana = "//span[.='4K Ulitra HD 3840х2160 ']"       # Выбоор разрешения экрана (в данном случае 4k)
    product_1 = "//a[@id='clickym'][@data-id='1041898']"       # Кнопка "Купить" выбранного продукта (Телевизор LED 75" SAMSUNG QE75Q60ABUXRU)
    prod1_price = "//span[@id='product__price_1041898']//span[@class = 'product__new']"       # Цена продукта
    prod1_name = "//a[@href='/catalog/televizory-i-kino/televizory/led-televizory/133017/']//span[@itemprop='name']"       # Название продукта


    # Getters

    def get_brend_spisok(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.brend_spisok)))

    def get_vybor_brenda(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vybor_brenda)))

    def get_smart_spisok(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.smart_spisok)))

    def get_vybor_smart_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vybor_smart_tv)))

    def get_razreshenie_ekrana_spisok(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.razreshenie_ekrana_spisok)))

    def get_vybor_razreshenie_ekrana(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vybor_razreshenie_ekrana)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_prod1_price(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.prod1_price)))


    # Actions

    def click_brend_spisok(self):
        self.get_brend_spisok().click()
        print("Click Brend spisok")

    def click_vybor_brenda(self):
        self.get_vybor_brenda().click()
        print("Click Vybor brenda")

    def click_smart_spisok(self):
        self.get_smart_spisok().click()
        print("Click Smart spisok")

    def click_vybor_smart_tv(self):
        self.get_vybor_smart_tv().click()
        print("Click Vybor smart tv")

    def click_razreshenie_ekrana_spisok(self):
        self.get_razreshenie_ekrana_spisok().click()
        print("Click Razreshenie ekrana spisok")

    def click_vybor_razreshenie_ekrana(self):
        self.get_vybor_razreshenie_ekrana().click()
        print("Click Vybor razreshenie ekrana")

    def click_product_1(self):
        self.get_product_1().click()
        print("Click Product 1")

    def text_prod1_price(self):
        self.get_prod1_price().text


    # Methods

    def select_characteristics(self):
        self.click_brend_spisok()
        time.sleep(1)
        self.click_vybor_brenda()
        self.click_smart_spisok()
        time.sleep(1)
        self.click_vybor_smart_tv()
        self.click_razreshenie_ekrana_spisok()
        time.sleep(1)
        self.click_vybor_razreshenie_ekrana()
        time.sleep(3)

    def select_brend_spisok(self):
        self.click_brend_spisok()


    def select_vybor_brenda(self):
        self.click_vybor_brenda()

    def select_smart_spisok(self):
        self.click_smart_spisok()

    def select_vybor_smart_tv(self):
        self.click_vybor_smart_tv()

    def select_razreshenie_ekrana_spisok(self):
        self.click_razreshenie_ekrana_spisok()

    def select_vybor_razreshenie_ekrana(self):
        self.click_vybor_razreshenie_ekrana()

    def select_product_1(self):
        self.select_characteristics()
        prod_price = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.prod1_price))).text    # Записываем значение цены продукта в переменную до попадания в корзину
        prod_price = re.sub("[^0-9]", "", prod_price)    # Удаляем все символы кроме цифр из переменной
        prod_name = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.prod1_name))).text    # Записываем название продукты в переменную до попадания в корзину
        self.click_product_1()
        self.enter_cart()
        time.sleep(3)
        self.get_screenshot()      # Взято из базового класса
        cart_price = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cartPage__itemPriceNow item_price']"))).text    # Записывает значение цены продукта в корзине в переменную
        cart_price = re.sub("[^0-9]", "", cart_price)      # Удаляем все символы кроме цифр из переменной
        assert prod_price == cart_price    # Сравниваем цену продукта до попадания в корзину с ценой продукта в корзине
        print("Product price - right")
        cart_name = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cartPage__itemTitle']"))).text      # Записываем название продукты в корзины в переменную
        assert prod_name == cart_name    # Сравниваем название продукта до попадания в корзину с названием продукта в корзине
        print("Product name - right")