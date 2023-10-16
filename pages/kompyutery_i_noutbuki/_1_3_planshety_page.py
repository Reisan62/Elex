from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Planshety_page(Base):


    # Locators

    planshetnye_pk = "//div[@class = 'tabs__content_inner js-accord-content']/a[@href = '/catalog/kompyutery-i-noutbuki/planshety/planshetnye-pk/']"       # Планшетные ПК
    aksessuary_dlya_planshetov = "//div/a[@href ='/catalog/kompyutery-i-noutbuki/planshety/aksessuary-dlya-planshetov/']"       # Аксессуары для планшетов


    # Getters

    def get_planshetnye_pk(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.planshetnye_pk)))

    def get_aksessuary_dlya_planshetov(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aksessuary_dlya_planshetov)))


    # Actions

    def click_planshetnye_pk(self):
        self.get_planshetnye_pk().click()
        print("Click Planshetnye PK")

    def click_aksessuary_dlya_planshetov(self):
        self.get_aksessuary_dlya_planshetov().click()
        print("Click Aksessuary dlya planshetov")


    # Methods

    def select_planshetnye_pk(self):
        self.get_current_url()
        self.click_planshetnye_pk()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/planshety/planshetnye-pk/")

    def select_aksessuary_dlya_planshetov(self):
        self.get_current_url()
        self.click_aksessuary_dlya_planshetov()
        self.assert_url("https://elex.ru/catalog/kompyutery-i-noutbuki/planshety/aksessuary-dlya-planshetov/")