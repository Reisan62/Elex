import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):      # Получаем текущую URL
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):        # Производим сравнение слов
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method screenshot"""

    def get_screenshot(self):       # Делаем скриншот
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\baldy\\AquaProjects\\main_project\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):       # Производим сравнение URL
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")