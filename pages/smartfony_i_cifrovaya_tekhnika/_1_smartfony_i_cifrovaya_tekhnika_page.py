from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Smartfony_i_cifrovaya_tekhnika_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    smart_i_sotov_tel = "//div/a[@href = '/catalog/telefoniya-foto-i-video/smartfony-i-sotovye-telefony/']"       # Смартфоны и сотовые телефоны
    port_accum = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/portativnye-akkumulyatory01140/']"       # Портативные аккумуляторы
    headphones = "//div/a[@href ='/catalog/telefoniya-foto-i-video/naushniki02851/']"       # Наушники и гарнитуры
    besprovod_akust = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/besprovodnye-kolonki/']"       # Беспроводная акустика
    сameras = "//div/a[@href ='/catalog/telefoniya-foto-i-video/fotoapparaty/']"       # Фотоаппараты
    action_cameras = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/ekshen-kamery/']"       # Экшен камеры
    quadcopters = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/gadzhety01138/']"       # Квадрокоптеры
    smart_watches_i_fit_bracel = "//div/a[@href='/catalog/telefoniya-foto-i-video/smart-chasy-i-fitnes-braslety/']"       # Смарт-часы и фитнес браслеты
    automobil_electr = "//div/a[@href ='/catalog/telefoniya-foto-i-video/avtomobilnaya-elektronika01053/']"       # Автомобильная электроника
    optica = "//div/a[@href ='/catalog/telefoniya-foto-i-video/optika/']"       # Оптика
    home_phone = "//div/a[@href ='/catalog/telefoniya-foto-i-video/domashnie-telefony/']"       # Домашние телефоны
    radiostancii = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href ='/catalog/telefoniya-foto-i-video/radiostantsii00261/']"       # Радиостанции
    videonablyudenie_i_umnyj_dom = "//div/a[@href ='/catalog/telefoniya-foto-i-video/videonablyudenie-i-umnyy-dom/']"       # Видеонаблюдение и умный дом
    e_books = "//div/a[@href='/catalog/telefoniya-foto-i-video/elektronnye-knigi03112/']"       # Электронные книги
    fotoaksessuary = "//div/a[@href ='/catalog/telefoniya-foto-i-video/fotoaksessuary/']"       # Фотоаксессуары



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
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.action_cameras)))

    def get_quadcopters(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.quadcopters)))

    def get_smart_watches_i_fit_bracel(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.smart_watches_i_fit_bracel)))

    def get_automobil_electr(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.automobil_electr)))

    def get_optica(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.optica)))

    def get_home_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.home_phone)))

    def get_radiostancii(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.radiostancii)))

    def get_videonablyudenie_i_umnyj_dom(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.videonablyudenie_i_umnyj_dom)))

    def get_e_books(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.e_books)))

    def get_fotoaksessuary(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.fotoaksessuary)))


    # Actions

    def click_smart_i_sotov_tel(self):
        self.get_smart_i_sotov_tel().click()
        print("Click Smartfony i sotovye telefony")

    def click_port_accum(self):
        self.get_port_accum().click()
        print("Click Portativnye akkumulyatory")

    def click_headphones(self):
        self.get_headphones().click()
        print("Click Headphones")

    def click_besprovod_akust(self):
        self.get_besprovod_akust().click()
        print("Click Besprovodnaya akustika")

    def click_сameras(self):
        self.get_сameras().click()
        print("Click Cameras")

    def click_action_cameras(self):
        self.get_action_cameras().click()
        print("Click Action cameras")

    def click_quadcopters(self):
        self.get_quadcopters().click()
        print("Click Quadcopters")

    def click_smart_watches_i_fit_bracel(self):
        self.get_smart_watches_i_fit_bracel().click()
        print("Click Smart watches i fitnes bracel")

    def click_automobil_electr(self):
        self.get_automobil_electr().click()
        print("Click Avtomobilnaya elektronika")

    def click_optica(self):
        self.get_optica().click()
        print("Click Optica")

    def click_home_phone(self):
        self.get_home_phone().click()
        print("Click Home phone")

    def click_radiostancii(self):
        self.get_radiostancii().click()
        print("Click Radiostancii")

    def click_videonablyudenie_i_umnyj_dom(self):
        self.get_videonablyudenie_i_umnyj_dom().click()
        print("Click Videonablyudenie i umnyj dom")

    def click_e_books(self):
        self.get_e_books().click()
        print("Click E-books")

    def click_fotoaksessuary(self):
        self.get_fotoaksessuary().click()
        print("Click Fotoaksessuary")


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

    def select_quadcopters(self):
        self.get_current_url()
        self.click_quadcopters()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/gadzhety01138/")

    def select_smart_watches_i_fit_bracel(self):
        self.get_current_url()
        self.click_smart_watches_i_fit_bracel()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/smart-chasy-i-fitnes-braslety/")

    def select_automobil_electr(self):
        self.get_current_url()
        self.click_automobil_electr()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/avtomobilnaya-elektronika01053/")

    def select_optica(self):
        self.get_current_url()
        self.click_optica()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/optika/")

    def select_home_phone(self):
        self.get_current_url()
        self.click_home_phone()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/domashnie-telefony/")

    def select_radiostancii(self):
        self.get_current_url()
        self.click_radiostancii()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/radiostantsii00261/")

    def select_videonablyudenie_i_umnyj_dom(self):
        self.get_current_url()
        self.click_videonablyudenie_i_umnyj_dom()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/videonablyudenie-i-umnyy-dom/")

    def select_e_books(self):
        self.get_current_url()
        self.click_e_books()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/elektronnye-knigi03112/")

    def select_fotoaksessuary(self):
        self.get_current_url()
        self.click_fotoaksessuary()
        self.assert_url("https://elex.ru/catalog/telefoniya-foto-i-video/fotoaksessuary/")



