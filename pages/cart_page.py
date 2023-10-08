import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    buy_button = "//button[@id='sub_order_button']"       # Кнопка "Купить"
    buy_without_authorization_button = "//a[.='Купить без авторизации']"       # Кнопка "Купить без авторизации"
    fio_field = "//input[@id='ORDER_PROP_20']"       # Поле ФИО
    email_field = "//input[@id='ORDER_PROP_19']"       # Поле E-mail
    phone_field = "//input[@id='ORDER_PROP_18']"       # Поле Телефон
    city_field = "//input[@id='ORDER_PROP_99']"       # Поле Город
    comments_field = "//textarea[@id='ORDER_DESCRIPTION']"       # Поле Комментарии
    courier_button = "//label[@for='ID_DELIVERY_ID_12']"       # Выбор доставки "Курьером в Москву"
    street = "//input[@id='ORDER_PROP_56']"       # Поле Улица
    home_number = "//input[@id='ORDER_PROP_16']"       # Поле Номер дома
    kv_number = "//input[@id='ORDER_PROP_44']"       # Поле Номер квартиры


    # Getters

    def get_buy_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_buy_without_authorization_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_without_authorization_button)))

    def get_fio_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fio_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_city_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_field)))

    def get_comments_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.comments_field)))

    def get_courier_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.courier_button)))

    def get_street(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_home_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.home_number)))

    def get_kv_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.kv_number)))


    # Actions

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click Buy button")

    def click_buy_without_authorization_button(self):
        self.get_buy_without_authorization_button().click()
        print("Click Buy without authorization button")

    def input_fio_field(self,fio_field):
        self.get_fio_field().send_keys(fio_field)
        print("Input FIO")

    def input_email_field(self,email_field):
        self.get_email_field().send_keys(email_field)
        print("Input E-mail")

    def input_phone_field(self,phone_field):
        self.get_phone_field().send_keys(phone_field)
        print("Input Phone")

    def input_city_field(self,city_field):
        self.get_city_field().send_keys(city_field)
        print("Input City")

    def input_comments_field(self,comments_field):
        self.get_comments_field().send_keys(comments_field)
        print("Input Comments")

    def click_courier_button(self):
        self.get_courier_button().click()
        print("Click Courier button")

    def input_street(self,street):
        self.get_street().send_keys(street)
        print("Input Street")

    def input_home_number(self,home_number):
        self.get_home_number().send_keys(home_number)
        print("Input Home number")

    def input_kv_number(self,kv_number):
        self.get_kv_number().send_keys(kv_number)
        print("Input Kv number")

    # Methods

    def buy_without_authorization(self):
        self.click_buy_button()
        time.sleep(2)
        self.click_buy_without_authorization_button()
        time.sleep(2)
        self.click_buy_button()
        time.sleep(1)
        self.input_personal_information()
        self.select_courier_button()
        time.sleep(1)
        self.input_delivery_information()
        self.assert_final_price()
        self.get_screenshot()

    def input_personal_information(self):
        self.input_fio_field("Иванов Иван Иванович")
        self.input_email_field("test@test.com")
        self.input_phone_field("9999999999")
        # self.input_city_field("Москва")       # Закомментировал, потому что, по умолчанию, уже введена "Москва"
        self.input_comments_field("Тестовая операция")

    def select_courier_button(self):
        self.click_courier_button()

    def input_delivery_information(self):
        self.input_street("Пушкина")
        self.input_home_number("77")
        self.input_kv_number("11")