from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Instrumenty_page(Base):


    # Locators

    elektroinstrument = "//div/a[@href = '/catalog/instrumenty/elektroinstrument01238/']"       # Электроинструмент
    stanki = "//div/a[@href ='/catalog/instrumenty/stanki/']"       # Станки
    ruchnoj_instrument = "//div/a[@href ='/catalog/instrumenty/ruchnoy-instrument/']"       # Ручной инструмент
    nabory_instrumentov = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/instrumenty/nabory-instrumentov/']"       # Наборы инструментов
    raskhodnye_materialy = "//div/a[@href ='/catalog/instrumenty/raskhodnye-materialy/']"       # Расходные материалы
    silovaya_tekhnika = "//div/a[@href = '/catalog/instrumenty/silovaya-tekhnika/']"       # Силовая техника

    # Getters

    def get_elektroinstrument(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.elektroinstrument)))

    def get_stanki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.stanki)))

    def get_ruchnoj_instrument(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.ruchnoj_instrument)))

    def get_nabory_instrumentov(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.nabory_instrumentov)))

    def get_raskhodnye_materialy(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.raskhodnye_materialy)))

    def get_silovaya_tekhnika(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.silovaya_tekhnika)))


    # Actions

    def click_elektroinstrument(self):
        self.get_elektroinstrument().click()
        print("Click Elektroinstrument")

    def click_stanki(self):
        self.get_stanki().click()
        print("Click Stanki")

    def click_ruchnoj_instrument(self):
        self.get_ruchnoj_instrument().click()
        print("Click Ruchnoj instrument")

    def click_nabory_instrumentov(self):
        self.get_nabory_instrumentov().click()
        print("Click Nabory instrumentov")

    def click_raskhodnye_materialy(self):
        self.get_raskhodnye_materialy().click()
        print("Click Raskhodnye materialy")

    def click_silovaya_tekhnika(self):
        self.get_silovaya_tekhnika().click()
        print("Click Silovaya tekhnika")


    # Methods

    def select_elektroinstrument(self):
        self.get_current_url()
        self.click_elektroinstrument()
        self.assert_url("https://elex.ru/catalog/instrumenty/elektroinstrument01238/")

    def select_stanki(self):
        self.get_current_url()
        self.click_stanki()
        self.assert_url("https://elex.ru/catalog/instrumenty/stanki/")

    def select_ruchnoj_instrument(self):
        self.get_current_url()
        self.click_ruchnoj_instrument()
        self.assert_url("https://elex.ru/catalog/instrumenty/ruchnoy-instrument/")

    def select_nabory_instrumentov(self):
        self.get_current_url()
        self.click_nabory_instrumentov()
        self.assert_url("https://elex.ru/catalog/instrumenty/nabory-instrumentov/")

    def select_raskhodnye_materialy(self):
        self.get_current_url()
        self.click_raskhodnye_materialy()
        self.assert_url("https://elex.ru/catalog/instrumenty/raskhodnye-materialy/")

    def select_silovaya_tekhnika(self):
        self.get_current_url()
        self.click_silovaya_tekhnika()
        self.assert_url("https://elex.ru/catalog/instrumenty/silovaya-tekhnika/")
