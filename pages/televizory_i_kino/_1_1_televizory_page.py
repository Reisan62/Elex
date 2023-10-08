from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Televizory_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    all_tv = "//div[@class='tabs__content_inner js-accord-content']/a[@href='/catalog/televizory-i-kino/televizory/led-televizory/']"       # Все телевизоры
    fourk_tv = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/televizory-i-kino/televizory/4k-televizory/']"       # 4K телевизоры
    eightk_tv = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/televizory-i-kino/televizory/8k-televizory/']"       # 8К телевизоры
    smart_tv = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/televizory-i-kino/televizory/smart-televizory/']"       # SMART телевизоры
    qled_tv = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/televizory-i-kino/televizory/qled-televizory/']"       # QLED телевизоры
    oled_tv = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/televizory-i-kino/televizory/oled-televizory/']"       # OLED телевизоры


    # Getters

    def get_all_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.all_tv)))

    def get_fourk_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.fourk_tv)))

    def get_eightk_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.eightk_tv)))

    def get_smart_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.smart_tv)))

    def get_qled_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.qled_tv)))

    def get_oled_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.oled_tv)))


    # Actions

    def click_all_tv(self):
        self.get_all_tv().click()
        print("Click ALL TV")

    def click_fourk_tv(self):
        self.get_fourk_tv().click()
        print("Click 4K TV")

    def click_eightk_tv(self):
        self.get_eightk_tv().click()
        print("Click 8K TV")

    def click_smart_tv(self):
        self.get_smart_tv().click()
        print("Click SMART TV")

    def click_qled_tv(self):
        self.get_qled_tv().click()
        print("Click QLED TV")

    def click_oled_tv(self):
        self.get_oled_tv().click()
        print("Click OLED TV")

    # Methods

    def select_all_tv(self):
        self.get_current_url()
        self.click_all_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/led-televizory/")

    def select_fourk_tv(self):
        self.get_current_url()
        self.click_fourk_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/4k-televizory/")

    def select_eightk_tv(self):
        self.get_current_url()
        self.click_eightk_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/8k-televizory/")

    def select_smart_tv(self):
        self.get_current_url()
        self.click_smart_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/smart-televizory/")

    def select_qled_tv(self):
        self.get_current_url()
        self.click_qled_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/qled-televizory/")

    def select_oled_tv(self):
        self.get_current_url()
        self.click_oled_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/oled-televizory/")


