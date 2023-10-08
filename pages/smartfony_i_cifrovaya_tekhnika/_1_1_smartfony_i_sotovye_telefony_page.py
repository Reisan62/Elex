from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Smartfony_i_sotovye_telefony_page(Base):

    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver


    # Locators

    smartfony = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href = '/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/smartfony-i-kommunikatory/']"       # Смартфоны
    sotovye_telefony = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/sotovye-telefony/']"       # Сотовые телефоны
    aksessuary_dlya_telefonov = "//div/a[@href ='/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/aksessuary-dlya-telefonov/']"       # Аксессуары для телефонов
    kontrakty = "//div/a[@href ='/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/kontrakty/']"       # Контракты
    ustrojstva_dopolnennoj_realnosti = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/ustroystva-dopolnennoy-realnosti/']"       # Устройства дополненной реальности


    # Getters

    def get_smartfony(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.smartfony)))

    def get_sotovye_telefony(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sotovye_telefony)))

    def get_aksessuary_dlya_telefonov(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_telefonov)))

    def get_kontrakty(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.kontrakty)))

    def get_ustrojstva_dopolnennoj_realnosti(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.ustrojstva_dopolnennoj_realnosti)))


    # Actions

    def click_smartfony(self):
        self.get_smartfony().click()
        print("Click Smartfony")

    def click_sotovye_telefony(self):
        self.get_sotovye_telefony().click()
        print("Click Sotovye telefony")

    def click_aksessuary_dlya_telefonov(self):
        self.get_aksessuary_dlya_telefonov().click()
        print("Click Aksessuary dlya telefonov")

    def click_kontrakty(self):
        self.get_kontrakty().click()
        print("Click Kontrakty")

    def click_ustrojstva_dopolnennoj_realnosti(self):
        self.get_ustrojstva_dopolnennoj_realnosti().click()
        print("Click Ustrojstva dopolnennoj real'nosti")


    # Methods

    def select_smartfony(self):
        self.get_current_url()
        self.click_smartfony()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/smartfony-i-kommunikatory/")

    def select_sotovye_telefony(self):
        self.get_current_url()
        self.click_sotovye_telefony()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/sotovye-telefony/")

    def select_aksessuary_dlya_telefonov(self):
        self.get_current_url()
        self.click_aksessuary_dlya_telefonov()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/aksessuary-dlya-telefonov/")

    def select_kontrakty(self):
        self.get_current_url()
        self.click_kontrakty()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/kontrakty/")

    def select_ustrojstva_dopolnennoj_realnosti(self):
        self.get_current_url()
        self.click_ustrojstva_dopolnennoj_realnosti()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/ustroystva-dopolnennoy-realnosti/")