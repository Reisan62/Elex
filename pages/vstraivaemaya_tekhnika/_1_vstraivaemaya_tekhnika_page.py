from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Vstraivaemaya_tekhnika_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    duhovye_shkafy = "//div/a[@href = '/catalog/vstraivaemaya-tekhnika/dukhovye-shkafy03140/']"  # Духовые шкафы
    varochnye_poverhnosti = "//div/a[@href ='/catalog/vstraivaemaya-tekhnika/varochnye-poverkhnosti/']"  # Варочные поверхности
    vstraivaemye_posudomoechnye_mashiny = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/vstraivaemaya-tekhnika/posudomoechnye-mashiny02801/']"  # Встраиваемые посудомоечные машины
    vytyazhki_i_aksessuary = "//div/a[@href ='/catalog/vstraivaemaya-tekhnika/vytyazhki02813/']"  # Вытяжки и аксессуары
    posuda_dlya_kuhni = "//div/a[@href ='/catalog/vstraivaemaya-tekhnika/posuda02857/']"  # Посуда для кухни
    vstraivaemye_holodilniki_i_stiralnyemashiny = "//div/a[@href ='/catalog/vstraivaemaya-tekhnika/vstraivaemye-kholodilniki-i-stiralnye-mashiny/']"  # Встраиваемые холодильники и стиральные машины
    vstraivaemye_svch = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/vstraivaemaya-tekhnika/vstraivaemye-svch/']"  # Встраиваемые СВЧ
    bytovaya_himiya = "//div/a[@href='/catalog/vstraivaemaya-tekhnika/bytovaya-khimiya02912/']"  # Бытовая химия
    aksessuary_dlya_vstraivaemoj_tekhniki = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/vstraivaemaya-tekhnika/aksessuary00205/']"  # Аксессуары для встраиваемой техники


    # Getters

    def get_duhovye_shkafy(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.duhovye_shkafy)))

    def get_varochnye_poverhnosti(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.varochnye_poverhnosti)))

    def get_vstraivaemye_posudomoechnye_mashiny(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vstraivaemye_posudomoechnye_mashiny)))

    def get_vytyazhki_i_aksessuary(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vytyazhki_i_aksessuary)))

    def get_posuda_dlya_kuhni(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.posuda_dlya_kuhni)))

    def get_vstraivaemye_holodilniki_i_stiralnyemashiny(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vstraivaemye_holodilniki_i_stiralnyemashiny)))

    def get_vstraivaemye_svch(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.vstraivaemye_svch)))

    def get_bytovaya_himiya(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.bytovaya_himiya)))

    def get_aksessuary_dlya_vstraivaemoj_tekhniki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_vstraivaemoj_tekhniki)))


    # Actions

    def click_duhovye_shkafy(self):
        self.get_duhovye_shkafy().click()
        print("Click Duhovye shkafy")

    def click_varochnye_poverhnosti(self):
        self.get_varochnye_poverhnosti().click()
        print("Click Varochnye poverhnosti")

    def click_vstraivaemye_posudomoechnye_mashiny(self):
        self.get_vstraivaemye_posudomoechnye_mashiny().click()
        print("Click Vstraivaemye posudomoechnye mashiny")

    def click_vytyazhki_i_aksessuary(self):
        self.get_vytyazhki_i_aksessuary().click()
        print("Click Vytyazhki i aksessuary")

    def click_posuda_dlya_kuhni(self):
        self.get_posuda_dlya_kuhni().click()
        print("Click Posuda dlya kuhni")

    def click_vstraivaemye_holodilniki_i_stiralnyemashiny(self):
        self.get_vstraivaemye_holodilniki_i_stiralnyemashiny().click()
        print("Click Vstraivaemye holodil'niki i stiral'nye mashiny")

    def click_vstraivaemye_svch(self):
        self.get_vstraivaemye_svch().click()
        print("Click Vstraivaemye SVCH")

    def click_bytovaya_himiya(self):
        self.get_bytovaya_himiya().click()
        print("Click Bytovaya himiya")

    def click_aksessuary_dlya_vstraivaemoj_tekhniki(self):
        self.get_aksessuary_dlya_vstraivaemoj_tekhniki().click()
        print("Click Aksessuary dlya vstraivaemoj tekhniki")


    # Methods

    def select_duhovye_shkafy(self):
        self.get_current_url()
        self.click_duhovye_shkafy()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/dukhovye-shkafy03140/")

    def select_varochnye_poverhnosti(self):
        self.get_current_url()
        self.click_varochnye_poverhnosti()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/varochnye-poverkhnosti/")

    def select_vstraivaemye_posudomoechnye_mashiny(self):
        self.get_current_url()
        self.click_vstraivaemye_posudomoechnye_mashiny()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/posudomoechnye-mashiny02801/")

    def select_vytyazhki_i_aksessuary(self):
        self.get_current_url()
        self.click_vytyazhki_i_aksessuary()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/vytyazhki02813/")

    def select_posuda_dlya_kuhni(self):
        self.get_current_url()
        self.click_posuda_dlya_kuhni()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/posuda02857/")

    def select_vstraivaemye_holodilniki_i_stiralnyemashiny(self):
        self.get_current_url()
        self.click_vstraivaemye_holodilniki_i_stiralnyemashiny()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/vstraivaemye-kholodilniki-i-stiralnye-mashiny/")

    def select_vstraivaemye_svch(self):
        self.get_current_url()
        self.click_vstraivaemye_svch()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/vstraivaemye-svch/")

    def select_bytovaya_himiya(self):
        self.get_current_url()
        self.click_bytovaya_himiya()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/bytovaya-khimiya02912/")

    def select_aksessuary_dlya_vstraivaemoj_tekhniki(self):
        self.get_current_url()
        self.click_aksessuary_dlya_vstraivaemoj_tekhniki()
        self.assert_url("https://elex.ru/catalog/vstraivaemaya-tekhnika/aksessuary00205/")