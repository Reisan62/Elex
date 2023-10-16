from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Akkumulyatornyj_transport_i_aktivnyj_otdyh_page(Base):


    # Locators

    transport = "//div/a[@href = '/catalog/aktivnyy-otdykh/akkumulyatornyy-transport/']"       # Транспорт
    tovary_dlya_avto = "//div/a[@href ='/catalog/aktivnyy-otdykh/tovary-dlya-avto01360/']"       # Товары для авто
    tovary_dlya_piknika_i_turizma = "//div/a[@href ='/catalog/aktivnyy-otdykh/tovary-dlya-piknika-i-turizma/']"       # Товары для пикника и туризма
    tovary_dlya_dachi = "//div/a[@href ='/catalog/aktivnyy-otdykh/tovary-dlya-dachi/']"       # Товары для дачи
    sportivnye_tovary = "//div/a[@href ='/catalog/aktivnyy-otdykh/sportivnye-tovary/']"       # Спортивные товары
    metalloiskateli = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href = '/catalog/aktivnyy-otdykh/metalloiskateli/']"       # Металлоискатели
    zimnie_tovary = "//div/a[@href = '/catalog/aktivnyy-otdykh/zimnie-tovary/']"       # Зимние товары


    # Getters

    def get_transport(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.transport)))

    def get_tovary_dlya_avto(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_avto)))

    def get_tovary_dlya_piknika_i_turizma(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_piknika_i_turizma)))

    def get_tovary_dlya_dachi(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_dachi)))

    def get_sportivnye_tovary(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sportivnye_tovary)))

    def get_metalloiskateli(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.metalloiskateli)))

    def get_zimnie_tovary(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.zimnie_tovary)))


    # Actions

    def click_transport(self):
        self.get_transport().click()
        print("Click Transport")

    def click_tovary_dlya_avto(self):
        self.get_tovary_dlya_avto().click()
        print("Click Tovary dlya avto")

    def click_tovary_dlya_piknika_i_turizma(self):
        self.get_tovary_dlya_piknika_i_turizma().click()
        print("Click Tovary dlya piknika i turizma")

    def click_tovary_dlya_dachi(self):
        self.get_tovary_dlya_dachi().click()
        print("Click Tovary dlya dachi")

    def click_sportivnye_tovary(self):
        self.get_sportivnye_tovary().click()
        print("Click Sportivnye tovary")

    def click_metalloiskateli(self):
        self.get_metalloiskateli().click()
        print("Click Metalloiskateli")

    def click_zimnie_tovary(self):
        self.get_zimnie_tovary().click()
        print("Click Zimnie tovary")


    # Methods

    def select_transport(self):
        self.get_current_url()
        self.click_transport()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/akkumulyatornyy-transport/")

    def select_tovary_dlya_avto(self):
        self.get_current_url()
        self.click_tovary_dlya_avto()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/tovary-dlya-avto01360/")

    def select_tovary_dlya_piknika_i_turizma(self):
        self.get_current_url()
        self.click_tovary_dlya_piknika_i_turizma()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/tovary-dlya-piknika-i-turizma/")

    def select_tovary_dlya_dachi(self):
        self.get_current_url()
        self.click_tovary_dlya_dachi()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/tovary-dlya-dachi/")

    def select_sportivnye_tovary(self):
        self.get_current_url()
        self.click_sportivnye_tovary()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/sportivnye-tovary/")

    def select_metalloiskateli(self):
        self.get_current_url()
        self.click_metalloiskateli()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/metalloiskateli/")

    def select_zimnie_tovary(self):
        self.get_current_url()
        self.click_zimnie_tovary()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/zimnie-tovary/")
