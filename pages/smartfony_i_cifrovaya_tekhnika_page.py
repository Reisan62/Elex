from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Smartfony_i_cifrovaya_tekhnika_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    smart_i_sotov_tel = "//div/a[@href = '/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/']"  # Смартфоны и сотовые телефоны
    port_accum = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/portativnye-akkumulyatory01140/']"  # Портативные аккумуляторы
    headphones = "//div/a[@href ='/catalog/telefoniya-foto-i-video/naushniki02851/]"  # Наушники и гарнитуры
    besprovod_akust = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/besprovodnye-kolonki/']"  # Беспроводная акустика
    сameras = "//div/a[@href ='/catalog/telefoniya-foto-i-video/fotoapparaty/']"  # Фотоаппараты
    action_cameras = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/ekshen-kamery/']"  # Экшен камеры


    # Getters

    def get_smart_i_sotov_tel(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.smart_i_sotov_tel)))

    def get_port_accum(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.port_accum)))

    def get_headphones(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.headphones)))

    def get_besprovod_akust(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.besprovod_akust)))

    def get_сameras(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.сameras)))

    def get_action_cameras(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.oled_tv)))


    # Actions

    def click_smart_i_sotov_tel(self):
        self.get_smart_i_sotov_tel().click()
        print("Click ALL TV")

    def click_port_accum(self):
        self.get_port_accum().click()
        print("Click 4K TV")

    def click_headphones(self):
        self.get_headphones().click()
        print("Click 8K TV")

    def click_besprovod_akust(self):
        self.get_besprovod_akust().click()
        print("Click SMART TV")

    def click_сameras(self):
        self.get_сameras().click()
        print("Click QLED TV")

    def click_action_cameras(self):
        self.get_action_cameras().click()
        print("Click OLED TV")

    # Methods

    def select_smart_i_sotov_tel(self):
        self.get_current_url()
        self.click_smart_i_sotov_tel()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/")

    def select_port_accum(self):
        self.get_current_url()
        self.click_port_accum()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/portativnye-akkumulyatory01140/")

    def select_headphones(self):
        self.get_current_url()
        self.click_headphones()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/naushniki02851/")

    def select_besprovod_akust(self):
        self.get_current_url()
        self.click_besprovod_akust()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/besprovodnye-kolonki/")

    def select_сameras(self):
        self.get_current_url()
        self.click_сameras()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/fotoapparaty/")

    def select_action_cameras(self):
        self.get_current_url()
        self.click_action_cameras()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/ekshen-kamery/")


