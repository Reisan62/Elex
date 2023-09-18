from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Muzykalnaya_tekhnika_page(Base):

    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver


    # Locators

    avtoaudiotekhnika = "//div/a[@href = '/catalog/muzykalnaya-tekhnika/avtoaudiotekhnika/']"  # Автоаудиотехника
    audio_dlya_doma = "//div/a[@href ='/catalog/muzykalnaya-tekhnika/audio-dlya-doma/']"  # Аудио для дома
    mikrofony = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/muzykalnaya-tekhnika/mikrofony01312/']"  # Микрофоны
    naushniki = "//div/a[@href ='/catalog/muzykalnaya-tekhnika/naushniki01011/']"  # Наушники
    portativnoe_audio = "//div/a[@href ='/catalog/muzykalnaya-tekhnika/portativnoe-audio/']"  # Портативное аудио
    aksessuary_dlya_muzykalnoj_tekhniki = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href = '/catalog/muzykalnaya-tekhnika/hi-fi/']"  # Аксессуары для музыкальной техники

    # Getters

    def get_avtoaudiotekhnika(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.avtoaudiotekhnika)))

    def get_audio_dlya_doma(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.audio_dlya_doma)))

    def get_mikrofony(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.mikrofony)))

    def get_naushniki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.naushniki)))

    def get_portativnoe_audio(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.portativnoe_audio)))

    def get_aksessuary_dlya_muzykalnoj_tekhniki(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_muzykalnoj_tekhniki)))


    # Actions

    def click_avtoaudiotekhnika(self):
        self.get_avtoaudiotekhnika().click()
        print("Click Avtoaudiotekhnika")

    def click_audio_dlya_doma(self):
        self.get_audio_dlya_doma().click()
        print("Click Audio dlya doma")

    def click_mikrofony(self):
        self.get_mikrofony().click()
        print("Click Mikrofony")

    def click_naushniki(self):
        self.get_naushniki().click()
        print("Click Naushniki")

    def click_portativnoe_audio(self):
        self.get_portativnoe_audio().click()
        print("Click Portativnoe audio")

    def click_aksessuary_dlya_muzykalnoj_tekhniki(self):
        self.get_aksessuary_dlya_muzykalnoj_tekhniki().click()
        print("Click Aksessuary dlya muzykalnoj tekhniki")


    # Methods

    def select_avtoaudiotekhnika(self):
        self.get_current_url()
        self.click_avtoaudiotekhnika()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/avtoaudiotekhnika/")

    def select_audio_dlya_doma(self):
        self.get_current_url()
        self.click_audio_dlya_doma()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/audio-dlya-doma/")

    def select_mikrofony(self):
        self.get_current_url()
        self.click_mikrofony()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/mikrofony01312/")

    def select_naushniki(self):
        self.get_current_url()
        self.click_naushniki()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/naushniki01011/")

    def select_portativnoe_audio(self):
        self.get_current_url()
        self.click_portativnoe_audio()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/portativnoe-audio/")

    def select_aksessuary_dlya_muzykalnoj_tekhniki(self):
        self.get_current_url()
        self.click_aksessuary_dlya_muzykalnoj_tekhniki()
        self.assert_url("https://elex.ru/catalog/muzykalnaya-tekhnika/hi-fi/")
