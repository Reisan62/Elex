from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Tekhnika_dlya_doma_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    stirka_i_sushka = "//div/a[@href = '/catalog/tovary-dlya-doma/stirka-i-sushka/']"       # Стирка и сушка
    pylesosy = "//div/a[@href ='/catalog/tovary-dlya-doma/pylesosy02936/']"       # Пылесосы
    tovary_dlya_uhoda_za_odezhdoj = "//div/a[@href ='/catalog/tovary-dlya-doma/utyugi02934/']"       # Товары для ухода за одеждой
    shvejnye_mashiny_i_aksessuary = "//div/a[@href ='/catalog/tovary-dlya-doma/shveynye-mashiny03013/']"       # Швейные машины и аксессуары
    bytovaya_tekhnika = "//div/a[@href ='/catalog/tovary-dlya-doma/bytovaya-tekhnika/']"       # Бытовая техника
    klimaticheskaya_tekhnika = "//div/a[@href ='/catalog/tovary-dlya-doma/klimaticheskaya-tekhnika/']"       # Климатическая техника
    videonablyudenie_i_umnyj_dom = "//div/a[@href ='/catalog/tovary-dlya-doma/videonablyudenie-i-avtomatizatsiya/']"       # Видеонаблюдение и умный дом
    tovary_dlya_prazdnika = "//div/a[@href='/catalog/tovary-dlya-doma/dlya-prazdnika/']"       # Товары для праздника
    tovary_dlya_detej = "//div/a[@href ='/catalog/tovary-dlya-doma/tovary-dlya-detey00618/']"       # Товары для детей


    # Getters

    def get_stirka_i_sushka(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.stirka_i_sushka)))

    def get_pylesosy(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pylesosy)))

    def get_tovary_dlya_uhoda_za_odezhdoj(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_uhoda_za_odezhdoj)))

    def get_shvejnye_mashiny_i_aksessuary(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.shvejnye_mashiny_i_aksessuary)))

    def get_bytovaya_tekhnika(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.bytovaya_tekhnika)))

    def get_klimaticheskaya_tekhnika(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.klimaticheskaya_tekhnika)))

    def get_videonablyudenie_i_umnyj_dom(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.videonablyudenie_i_umnyj_dom)))

    def get_tovary_dlya_prazdnika(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_prazdnika)))

    def get_tovary_dlya_detej(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tovary_dlya_detej)))


    # Actions

    def click_stirka_i_sushka(self):
        self.get_stirka_i_sushka().click()
        print("Click Stirka i sushka")

    def click_pylesosy(self):
        self.get_pylesosy().click()
        print("Click Pylesosy")

    def click_tovary_dlya_uhoda_za_odezhdoj(self):
        self.get_tovary_dlya_uhoda_za_odezhdoj().click()
        print("Click Tovary dlya uhoda za odezhdoj")

    def click_shvejnye_mashiny_i_aksessuary(self):
        self.get_shvejnye_mashiny_i_aksessuary().click()
        print("Click Shvejnye mashiny i aksessuary")

    def click_bytovaya_tekhnika(self):
        self.get_bytovaya_tekhnika().click()
        print("Click Bytovaya tekhnika")

    def click_klimaticheskaya_tekhnika(self):
        self.get_klimaticheskaya_tekhnika().click()
        print("Click Klimaticheskaya tekhnika")

    def click_videonablyudenie_i_umnyj_dom(self):
        self.get_videonablyudenie_i_umnyj_dom().click()
        print("Click Videonablyudenie i umnyj dom")

    def click_tovary_dlya_prazdnika(self):
        self.get_tovary_dlya_prazdnika().click()
        print("Click Tovary dlya prazdnika")

    def click_tovary_dlya_detej(self):
        self.get_tovary_dlya_detej().click()
        print("Click Tovary dlya detej")


    # Methods

    def select_stirka_i_sushka(self):
        self.get_current_url()
        self.click_stirka_i_sushka()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/stirka-i-sushka/")

    def select_pylesosy(self):
        self.get_current_url()
        self.click_pylesosy()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/pylesosy02936/")

    def select_tovary_dlya_uhoda_za_odezhdoj(self):
        self.get_current_url()
        self.click_tovary_dlya_uhoda_za_odezhdoj()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/utyugi02934/")

    def select_shvejnye_mashiny_i_aksessuary(self):
        self.get_current_url()
        self.click_shvejnye_mashiny_i_aksessuary()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/shveynye-mashiny03013/")

    def select_bytovaya_tekhnika(self):
        self.get_current_url()
        self.click_bytovaya_tekhnika()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/bytovaya-tekhnika/")

    def select_klimaticheskaya_tekhnika(self):
        self.get_current_url()
        self.click_klimaticheskaya_tekhnika()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/klimaticheskaya-tekhnika/")

    def select_videonablyudenie_i_umnyj_dom(self):
        self.get_current_url()
        self.click_videonablyudenie_i_umnyj_dom()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/videonablyudenie-i-avtomatizatsiya/")

    def select_tovary_dlya_prazdnika(self):
        self.get_current_url()
        self.click_tovary_dlya_prazdnika()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/dlya-prazdnika/")

    def select_tovary_dlya_detej(self):
        self.get_current_url()
        self.click_tovary_dlya_detej()
        self.assert_url("https://elex.ru/catalog/tovary-dlya-doma/tovary-dlya-detey00618/")