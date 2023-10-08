from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Main_page(Base):

    url = 'https://elex.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    tv_and_kino = "//li[@id='bx_1847241719_1347']"       # Телевизоры и Кино
    smart_and_tech = "//li[@id='bx_1847241719_1667']"       # Смартфоны и цифровая техника
    pk_and_nout = "//li[@id='bx_1847241719_1095']"       # Компьютеры и ноутбуки
    tech_for_kitchen = "//li[@id='bx_1847241719_1431']"       # Техника для кухни
    vstroi_tech = "//li[@id='bx_1847241719_1439']"       # Встраиваемая техника
    tech_for_home = "//li[@id='bx_1847241719_1582']"       # Техника для дома
    beauty_and_health = "//li[@id='bx_1847241719_1210']"       # Красота и здоровье
    music_tech = "//li[@id='bx_1847241719_1236']"       # Музыкальная техника
    acum_and_rest = "//li[@id='bx_1847241719_924']"       # Аккумуляторный транспорт и активный отдых
    instruments = "//li[@id='bx_1847241719_973']"       # Инструменты



    # Getters

    def get_tv_and_kino(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tv_and_kino)))

    def get_smart_and_tech(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.smart_and_tech)))

    def get_pk_and_nout(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pk_and_nout)))

    def get_tech_for_kitchen(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tech_for_kitchen)))

    def get_vstroi_tech(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vstroi_tech)))

    def get_tech_for_home(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tech_for_home)))

    def get_beauty_and_health(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.beauty_and_health)))

    def get_music_tech(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.music_tech)))

    def get_acum_and_rest(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.acum_and_rest)))

    def get_instruments(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.instruments)))


    # Actions

    def click_tv_and_kino(self):
        self.get_tv_and_kino().click()
        print("Click Televizory i Kino")

    def click_smart_and_tech(self):
        self.get_smart_and_tech().click()
        print("Click Smartfony i cifrovaya tekhnika")

    def click_pk_and_nout(self):
        self.get_pk_and_nout().click()
        print("Click Kompyutery i noutbuki")

    def click_tech_for_kitchen(self):
        self.get_tech_for_kitchen().click()
        print("Click Tekhnika dlya kuhni")

    def click_vstroi_tech(self):
        self.get_vstroi_tech().click()
        print("Click Vstraivaemaya tekhnika")

    def click_tech_for_home(self):
        self.get_tech_for_home().click()
        print("Click Tekhnika dlya doma")

    def click_beauty_and_health(self):
        self.get_beauty_and_health().click()
        print("Click Krasota i zdorove")

    def click_music_tech(self):
        self.get_music_tech().click()
        print("Click Muzykalnaya tekhnika")

    def click_acum_and_rest(self):
        self.get_acum_and_rest().click()
        print("Click Akkumulyatornyj transport i aktivnyj otdyh")

    def click_instruments(self):
        self.get_instruments().click()
        print("Click Instrumenty")


    # Methods

    def select_tv_and_kino(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_tv_and_kino()
        self.assert_url("https://elex.ru/catalog/televizory-i-kino/")

    def select_smart_and_tech(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_smart_and_tech()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/")

    def select_pk_and_nout(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_pk_and_nout()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/")

    def select_tech_for_kitchen(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_tech_for_kitchen()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/")

    def select_vstroi_tech(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_vstroi_tech()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/")

    def select_tech_for_home(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_tech_for_home()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/")

    def select_beauty_and_health(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_beauty_and_health()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/")

    def select_music_tech(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_music_tech()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/")

    def select_acum_and_rest(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_acum_and_rest()
        self.assert_url("https://elex.ru/catalog/aktivnyy-otdykh/")

    def select_instruments(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_instruments()
        self.assert_url("https://elex.ru/catalog/instrumenty/")

