import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Mytest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://120.76.206.144:8080/mms/login.html"
        self.driver.get(self.url)

    def tearDown(self) -> None:
        self.driver.quit()

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver,30,0.5).until(lambda x:x.find_element(*locator))
            return element
        except NoSuchElementException as e:
            print("Error detail:{}".format(e.args[0]))

    def test1(self):
        self.find_element(("id", "username")).send_keys("admin")
        self.find_element(("id", "password")).send_keys("123")

        self.find_element(("xpath", "//input[@value='Login']")).click()
        self.find_element(("xpath", "//div[@class='panel']/div[1]")).click()

        self.find_element(("partial link text", "查询顾客信息"))



