from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Tv_and_kino_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    tv = "//div/a[@href='/catalog/televizory-i-kino/televizory/']"  # Телевизоры
    sputnik_tv = "//div/a[@href='/catalog/televizory-i-kino/televidenie/']"  # Спутниковое и цифровое ТВ
    aksessuary_for_tv = "//div/a[@href='/catalog/televizory-i-kino/aksessuary/']"  # Аксессуары для телевизоров
    pleery_for_tv = "//div/a[@href='/catalog/televizory-i-kino/pleery/']"  # Плееры для телевизоров
    tv_stoyki = "//div[@class='tabs__content_inner js-accord-content']/a[@href='/catalog/televizory-i-kino/tv-stoyki/']"  # ТВ стойки


    # Getters

    def get_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tv)))

    def get_sputnik_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sputnik_tv)))

    def get_aksessuary_for_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_for_tv)))

    def get_pleery_for_tv(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pleery_for_tv)))

    def get_tv_stoyki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tv_stoyki)))


    # Actions

    def click_tv(self):
        self.get_tv().click()
        print("Click Televizory")

    def click_sputnik_tv(self):
        self.get_sputnik_tv().click()
        print("Click Sputnikovoe i cifrovoe TV")

    def click_aksessuary_for_tv(self):
        self.get_aksessuary_for_tv().click()
        print("Click Aksessuary dlya televizorov")

    def click_pleery_for_tv(self):
        self.get_pleery_for_tv().click()
        print("Click Pleery dlya televizorov")

    def click_tv_stoyki(self):
        self.get_tv_stoyki().click()
        print("Click TV stojki")


    # Methods

    def select_tv(self):
        self.get_current_url()
        self.click_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televizory/")

    def select_sputnik_tv(self):
        self.get_current_url()
        self.click_sputnik_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/televidenie/")

    def select_aksessuary_for_tv(self):
        self.get_current_url()
        self.click_aksessuary_for_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/aksessuary/")

    def select_pleery_for_tv(self):
        self.get_current_url()
        self.click_pleery_for_tv()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/pleery/")

    def select_tv_stoyki(self):
        self.get_current_url()
        self.click_tv_stoyki()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/tv-stoyki/")
