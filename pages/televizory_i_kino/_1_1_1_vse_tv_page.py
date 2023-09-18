from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Vse_tv_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    brend_spisok = "//span[.='Бренд']"  # Список брендов
    vybor_brenda = "//span[.='SAMSUNG ']"  # Выбираем бренд ( в данном случаей SAMSUNG)
    smart_spisok = "//span[.='Smart TV']"  # Список Smart TV
    vybor_smart_tv = "//input[@name='arrFilter_17_1004570158']//span[.='есть ']"  # Выбор наличиня Smart TV ( в данном случаей "есть")
    razreshenie_ekrana_spisok = "//span[.='Разрешение экрана']"  # Список разрешений экрана
    vybor_razreshenie_ekrana = "//input[@id='arrFilter_17_2609115691']"  # Выбоор разрешения экрана (в данном случае 4k)


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

    # Methods

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