from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Kompyutery_i_noutbuki_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    kompyutery_i_noutbuki = "//div/a[@href = '/catalog/kompyutery-i-noutbuki/kompyutery-i-noutbuki00012/']"  # Компьютеры и ноутбуки
    monitory = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/kompyutery-i-noutbuki/monitory/']"  # Мониторы
    planshety = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/planshety/']"  # Планшеты
    igrovye_kompyutery_i_aksessuary = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/igrovye-aksessuary/']"  # Игровые компьютеры и аксессуары
    printery_i_skanery = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/printery-i-skanery/']"  # Принтеры и сканеры
    setevoe_oborudovanie = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/kompyutery-i-noutbuki/setevoe-oborudovanie/']"  # Сетевое оборудование
    nositeli_informacii = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/nositeli-informatsii/']"  # Носители информации
    aksessuary_dlya_kompyuterov = "//div/a[@href='/catalog/kompyutery-i-noutbuki/aksessuary-dlya-kompyuterov/']"  # Аксессуары для компьютеров
    kompyuternaya_mebel = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/kompyuternaya-mebel/']"  # Компьютерная мебель
    programmnoe_obespechenie = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/programmnoe-obespechenie/']"  # Программное обеспечение


    # Getters

    def get_kompyutery_i_noutbuki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.kompyutery_i_noutbuki)))

    def get_monitory(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.monitory)))

    def get_planshety(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.planshety)))

    def get_igrovye_kompyutery_i_aksessuary(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.igrovye_kompyutery_i_aksessuary)))

    def get_printery_i_skanery(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.printery_i_skanery)))

    def get_setevoe_oborudovanie(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.setevoe_oborudovanie)))

    def get_nositeli_informacii(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.nositeli_informacii)))

    def get_aksessuary_dlya_kompyuterov(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_kompyuterov)))

    def get_kompyuternaya_mebel(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.kompyuternaya_mebel)))

    def get_programmnoe_obespechenie(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.programmnoe_obespechenie)))


    # Actions

    def click_kompyutery_i_noutbuki(self):
        self.get_kompyutery_i_noutbuki().click()
        print("Click Kompyutery_i_noutbuki")

    def click_monitory(self):
        self.get_monitory().click()
        print("Click Monitory")

    def click_planshety(self):
        self.get_planshety().click()
        print("Click Planshety")

    def click_igrovye_kompyutery_i_aksessuary(self):
        self.get_igrovye_kompyutery_i_aksessuary().click()
        print("Click Igrovye komp'yutery i aksessuary")

    def click_printery_i_skanery(self):
        self.get_printery_i_skanery().click()
        print("Click Printery i skanery")

    def click_setevoe_oborudovanie(self):
        self.get_setevoe_oborudovanie().click()
        print("Click Setevoe oborudovanie")

    def click_nositeli_informacii(self):
        self.get_nositeli_informacii().click()
        print("Click Nositeli informacii")

    def click_aksessuary_dlya_kompyuterov(self):
        self.get_aksessuary_dlya_kompyuterov().click()
        print("Click Aksessuary dlya komp'yuterov")

    def click_kompyuternaya_mebel(self):
        self.get_kompyuternaya_mebel().click()
        print("Click Komp'yuternaya mebel'")

    def click_programmnoe_obespechenie(self):
        self.get_programmnoe_obespechenie().click()
        print("Click Programmnoe obespechenie")


    # Methods

    def select_kompyutery_i_noutbuki(self):
        self.get_current_url()
        self.click_kompyutery_i_noutbuki()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/kompyutery-i-noutbuki00012/")

    def select_monitory(self):
        self.get_current_url()
        self.click_monitory()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/monitory/")

    def select_planshety(self):
        self.get_current_url()
        self.click_planshety()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/planshety/")

    def select_igrovye_kompyutery_i_aksessuary(self):
        self.get_current_url()
        self.click_igrovye_kompyutery_i_aksessuary()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/igrovye-aksessuary/")

    def select_printery_i_skanery(self):
        self.get_current_url()
        self.click_printery_i_skanery()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/printery-i-skanery/")

    def select_setevoe_oborudovanie(self):
        self.get_current_url()
        self.click_setevoe_oborudovanie()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/setevoe-oborudovanie/")

    def select_nositeli_informacii(self):
        self.get_current_url()
        self.click_nositeli_informacii()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/nositeli-informatsii/")

    def select_aksessuary_dlya_kompyuterov(self):
        self.get_current_url()
        self.click_aksessuary_dlya_kompyuterov()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/aksessuary-dlya-kompyuterov/")

    def select_kompyuternaya_mebel(self):
        self.get_current_url()
        self.click_kompyuternaya_mebel()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/kompyuternaya-mebel/")

    def select_programmnoe_obespechenie(self):
        self.get_current_url()
        self.click_programmnoe_obespechenie()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/programmnoe-obespechenie/")