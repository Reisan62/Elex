from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import Main_page
from pages.smartfony_i_cifrovaya_tekhnika._1_smartfony_i_cifrovaya_tekhnika_page import Smartfony_i_cifrovaya_tekhnika_page
from pages.smartfony_i_cifrovaya_tekhnika._1_1_smartfony_i_sotovye_telefony_page import Smartfony_i_sotovye_telefony_page
from pages.televizory_i_kino._1_tv_and_kino_page import Tv_and_kino_page
from pages.televizory_i_kino._1_1_televizory_page import Televizory_page
from pages.kompyutery_i_noutbuki._1_kompyutery_i_noutbuki_page import Kompyutery_i_noutbuki_page
from pages.kompyutery_i_noutbuki._1_3_planshety_page import Planshety_page
from pages.tekhnika_dlya_kukhni._1_tekhnika_dlya_kukhni_page import Tekhnika_dlya_kukhni_page
from pages.vstraivaemaya_tekhnika._1_vstraivaemaya_tekhnika_page import Vstraivaemaya_tekhnika_page
from pages.tekhnika_dlya_doma._1_tekhnika_dlya_doma_page import Tekhnika_dlya_doma_page
from pages.krasota_i_zdorove._1_krasota_i_zdorove_page import Krasota_i_zdorove_page


def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "none"
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    g = Service('C:\\Users\\baldy\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g,)

    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_beauty_and_health()

    pk = Krasota_i_zdorove_page(driver)
    pk.select_aksessuary_dlya_krasoty_i_zdorovya()



    print("Finish Test 1")




