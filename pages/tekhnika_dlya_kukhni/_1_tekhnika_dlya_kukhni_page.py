from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Tekhnika_dlya_kukhni_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    prigotovlenie_pishchi = "//div/a[@href = '/catalog/tekhnika-dlya-kukhni/krupnaya-kukhonnaya-tekhnika/']"  # Приготовление пищи
    holodilnoe_oborudovanie = "//div/a[@href ='/catalog/tekhnika-dlya-kukhni/kholodilniki02802/']"  # Холодильное оборудование
    posudomoechnye_mashiny = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/tekhnika-dlya-kukhni/posudomoechnye-mashiny/']"  # Посудомоечные машины
    prigotovlenie_kofe = "//div/a[@href ='/catalog/tekhnika-dlya-kukhni/prigotovlenie-kofe/']"  # Приготовление кофе
    prochie_tovary_dlya_kuhni = "//div/a[@href ='/catalog/tekhnika-dlya-kukhni/kukhonnaya-tekhnika/']"  # Прочие товары для кухни
    bytovaya_himiya = "//div/a[@href ='/catalog/tekhnika-dlya-kukhni/bytovaya-khimiya00911/']"  # Бытовая химия
    posuda = "//div/a[@href ='/catalog/tekhnika-dlya-kukhni/posuda00879/']"  # Посуда
    aksessuary_dlya_kuhni = "//div/a[@href='/catalog/tekhnika-dlya-kukhni/aksessuary-dlya-kukhni01056/']"  # Аксессуары для кухни
    filtry_dlya_ochistki_vody = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/tekhnika-dlya-kukhni/filtry-dlya-ochistki-vody/']"  # Фильтры для очистки воды
    sifony_dlya_kuhni = "//div/a[@href ='/catalog/tekhnika-dlya-kukhni/sifony/']"  # Сифоны для кухни


    # Getters

    def get_prigotovlenie_pishchi(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.prigotovlenie_pishchi)))

    def get_holodilnoe_oborudovanie(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.holodilnoe_oborudovanie)))

    def get_posudomoechnye_mashiny(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.posudomoechnye_mashiny)))

    def get_prigotovlenie_kofe(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.prigotovlenie_kofe)))

    def get_prochie_tovary_dlya_kuhni(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.prochie_tovary_dlya_kuhni)))

    def get_bytovaya_himiya(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.bytovaya_himiya)))

    def get_posuda(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.posuda)))

    def get_aksessuary_dlya_kuhni(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_kuhni)))

    def get_filtry_dlya_ochistki_vody(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filtry_dlya_ochistki_vody)))

    def get_sifony_dlya_kuhni(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sifony_dlya_kuhni)))


    # Actions

    def click_prigotovlenie_pishchi(self):
        self.get_prigotovlenie_pishchi().click()
        print("Click Prigotovlenie pishchi")

    def click_holodilnoe_oborudovanie(self):
        self.get_holodilnoe_oborudovanie().click()
        print("Click Holodil'noe oborudovanie")

    def click_posudomoechnye_mashiny(self):
        self.get_posudomoechnye_mashiny().click()
        print("Click Posudomoechnye mashiny")

    def click_prigotovlenie_kofe(self):
        self.get_prigotovlenie_kofe().click()
        print("Click Prigotovlenie kofe")

    def click_prochie_tovary_dlya_kuhni(self):
        self.get_prochie_tovary_dlya_kuhni().click()
        print("Click Prochie tovary dlya kuhni")

    def click_bytovaya_himiya(self):
        self.get_bytovaya_himiya().click()
        print("Click Bytovaya himiya")

    def click_posuda(self):
        self.get_posuda().click()
        print("Click Posuda")

    def click_aksessuary_dlya_kuhni(self):
        self.get_aksessuary_dlya_kuhni().click()
        print("Click Aksessuary dlya kuhni")

    def click_filtry_dlya_ochistki_vody(self):
        self.get_filtry_dlya_ochistki_vody().click()
        print("Click Fil'try dlya ochistki vody")

    def click_sifony_dlya_kuhni(self):
        self.get_sifony_dlya_kuhni().click()
        print("Click Sifony dlya kuhni")


    # Methods

    def select_prigotovlenie_pishchi(self):
        self.get_current_url()
        self.click_prigotovlenie_pishchi()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/krupnaya-kukhonnaya-tekhnika/")

    def select_holodilnoe_oborudovanie(self):
        self.get_current_url()
        self.click_holodilnoe_oborudovanie()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/kholodilniki02802/")

    def select_posudomoechnye_mashiny(self):
        self.get_current_url()
        self.click_posudomoechnye_mashiny()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/posudomoechnye-mashiny/")

    def select_prigotovlenie_kofe(self):
        self.get_current_url()
        self.click_prigotovlenie_kofe()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/prigotovlenie-kofe/")

    def select_prochie_tovary_dlya_kuhni(self):
        self.get_current_url()
        self.click_prochie_tovary_dlya_kuhni()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/kukhonnaya-tekhnika/")

    def select_bytovaya_himiya(self):
        self.get_current_url()
        self.click_bytovaya_himiya()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/bytovaya-khimiya00911/")

    def select_posuda(self):
        self.get_current_url()
        self.click_posuda()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/posuda00879/")

    def select_aksessuary_dlya_kuhni(self):
        self.get_current_url()
        self.click_aksessuary_dlya_kuhni()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/aksessuary-dlya-kukhni01056/")

    def select_filtry_dlya_ochistki_vody(self):
        self.get_current_url()
        self.click_filtry_dlya_ochistki_vody()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/filtry-dlya-ochistki-vody/")

    def select_sifony_dlya_kuhni(self):
        self.get_current_url()
        self.click_sifony_dlya_kuhni()
        self.assert_url("https://elex.ru/catalog/tekhnika-dlya-kukhni/sifony/")