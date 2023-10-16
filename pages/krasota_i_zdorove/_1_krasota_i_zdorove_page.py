from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Krasota_i_zdorove_page(Base):


    # Locators

    tovary_dlya_strizhki_volos = "//div/a[@href = '/catalog/krasota-i-zdorove/strizhka-volos/']"       # Товары для стрижки волос
    tovary_dlya_ukladki_volos = "//div/a[@href ='/catalog/krasota-i-zdorove/ukladka-volos/']"       # Товары для укладки волос
    britvy = "//div/a[@href ='/catalog/krasota-i-zdorove/britvy02930/']"       # Бритвы
    epilyatory = "//div/a[@href ='/catalog/krasota-i-zdorove/epilyatory03011/']"       # Эпиляторы
    zubnye_shchetki = "//div/a[@href ='/catalog/krasota-i-zdorove/zubnye-shchetki02929/']"       # Зубные щетки
    kosmeticheskie_pribory = "//div/a[@href ='/catalog/krasota-i-zdorove/kosmeticheskie-pribory/']"       # Косметические приборы
    tovary_dlya_zdorovya_i_krasoty = "//div/a[@href ='/catalog/krasota-i-zdorove/zdorovyy-obraz-zhizni/']"       # Товары для здоровья и красоты
    medicinskie_pribory = "//div/a[@href='/catalog/krasota-i-zdorove/meditsinskie-pribory/']"       # Медицинские приборы
    vesy_napolnye = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/krasota-i-zdorove/vesy-napolnye/']"       # Весы напольные
    vannochki_dlya_nog = "//div[@class='tabs__content_inner js-accord-content']/a[@href='/catalog/krasota-i-zdorove/vannochki-dlya-nog/']"       # Ванночки для ног
    aksessuary_dlya_krasoty_i_zdorovya = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/krasota-i-zdorove/aksessuary00204/']"       # Аксессуары для красоты и здоровья


    # Getters

    def get_tovary_dlya_strizhki_volos(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_strizhki_volos)))

    def get_tovary_dlya_ukladki_volos(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_ukladki_volos)))

    def get_britvy(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.britvy)))

    def get_epilyatory(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.epilyatory)))

    def get_zubnye_shchetki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.zubnye_shchetki)))

    def get_kosmeticheskie_pribory(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.kosmeticheskie_pribory)))

    def get_tovary_dlya_zdorovya_i_krasoty(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_zdorovya_i_krasoty)))

    def get_medicinskie_pribory(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.medicinskie_pribory)))

    def get_vesy_napolnye(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vesy_napolnye)))

    def get_vannochki_dlya_nog(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vannochki_dlya_nog)))

    def get_aksessuary_dlya_krasoty_i_zdorovya(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_krasoty_i_zdorovya)))


    # Actions

    def click_tovary_dlya_strizhki_volos(self):
        self.get_tovary_dlya_strizhki_volos().click()
        print("Click Tovary dlya strizhki volos")

    def click_tovary_dlya_ukladki_volos(self):
        self.get_tovary_dlya_ukladki_volos().click()
        print("Click Tovary dlya ukladki volos")

    def click_britvy(self):
        self.get_britvy().click()
        print("Click Britvy")

    def click_epilyatory(self):
        self.get_epilyatory().click()
        print("Click Epilyatory")

    def click_zubnye_shchetki(self):
        self.get_zubnye_shchetki().click()
        print("Click Zubnye shchetki")

    def click_kosmeticheskie_pribory(self):
        self.get_kosmeticheskie_pribory().click()
        print("Click Kosmeticheskie pribory")

    def click_tovary_dlya_zdorovya_i_krasoty(self):
        self.get_tovary_dlya_zdorovya_i_krasoty().click()
        print("Click Tovary dlya zdorov'ya i krasoty")

    def click_medicinskie_pribory(self):
        self.get_medicinskie_pribory().click()
        print("Click Medicinskie pribory")

    def click_vesy_napolnye(self):
        self.get_vesy_napolnye().click()
        print("Click Vesy napol'nye")

    def click_vannochki_dlya_nog(self):
        self.get_vannochki_dlya_nog().click()
        print("Click Vannochki dlya nog")

    def click_aksessuary_dlya_krasoty_i_zdorovya(self):
        self.get_aksessuary_dlya_krasoty_i_zdorovya().click()
        print("Click Aksessuary dlya krasoty i zdorov'ya")

    # Methods

    def select_tovary_dlya_strizhki_volos(self):
        self.get_current_url()
        self.click_tovary_dlya_strizhki_volos()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/strizhka-volos/")

    def select_tovary_dlya_ukladki_volos(self):
        self.get_current_url()
        self.click_tovary_dlya_ukladki_volos()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/ukladka-volos/")

    def select_britvy(self):
        self.get_current_url()
        self.click_britvy()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/britvy02930/")

    def select_epilyatory(self):
        self.get_current_url()
        self.click_epilyatory()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/epilyatory03011/")

    def select_zubnye_shchetki(self):
        self.get_current_url()
        self.click_zubnye_shchetki()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/zubnye-shchetki02929/")

    def select_kosmeticheskie_pribory(self):
        self.get_current_url()
        self.click_kosmeticheskie_pribory()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/kosmeticheskie-pribory/")

    def select_tovary_dlya_zdorovya_i_krasoty(self):
        self.get_current_url()
        self.click_tovary_dlya_zdorovya_i_krasoty()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/zdorovyy-obraz-zhizni/")

    def select_medicinskie_pribory(self):
        self.get_current_url()
        self.click_medicinskie_pribory()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/meditsinskie-pribory/")

    def select_vesy_napolnye(self):
        self.get_current_url()
        self.click_vesy_napolnye()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/vesy-napolnye/")

    def select_vannochki_dlya_nog(self):
        self.get_current_url()
        self.click_vannochki_dlya_nog()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/vannochki-dlya-nog/")

    def select_aksessuary_dlya_krasoty_i_zdorovya(self):
        self.get_current_url()
        self.click_aksessuary_dlya_krasoty_i_zdorovya()
        self.assert_url("https://elex.ru/catalog/krasota-i-zdorove/aksessuary00204/")