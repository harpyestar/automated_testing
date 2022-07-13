from selenium import webdriver
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

class MMSLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://120.76.206.144:8080/mms/login.html"
        self.driver.implicitly_wait(5)
        self.imgs = []

    def tearDown(self) -> None:
        self.driver.quit()


    def test_login_success(self):
        """
            当用户名和密码成功的时候，能够登录到系统当中
        :return:
        """

        self.driver.get(self.url)
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element("id", "username").send_keys("admin")
        self.driver.find_element("id", "password").send_keys("123")
        self.driver.find_element("xpath", "//input[@value='Login']").click()

        loginName = self.driver.find_element("id", "loginName").text
        self.imgs.append(self.driver.get_screenshot_as_base64())

        self.assertEqual(loginName, "adminxx")

    def test_login_without_username(self):
        """
            当用户名没有进行输入的时候，进行‘UserId不能为空’的弹框提示
        :return:
        """
        self.driver.get(self.url)
        self.driver.find_element("id", "password").send_keys("123")
        self.driver.find_element("xpath", "//input[@value='Login']").click()

        errName = self.driver.find_element("xpath", "//div[contains(text(), '不能为空')]").text

        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.assertEqual("User Id不能为空", errName)
    #
    # def test_login_incorrect_username(self):
    #     pass
    #
    # def test_login_incorrect_password(self):
    #     pass



if __name__ == '__main__':
    # unittest.main()

    logintestloader = unittest.defaultTestLoader.loadTestsFromTestCase(MMSLoginTest)
    suite = unittest.TestSuite(logintestloader)

    runner = HTMLTestRunner(
        title = "带截图的测试报告",
        description = "xxx软件测试报告V1.0",
        stream=open("sample_test_report.html", "wb"),
        verbosity=2, # 详尽程度
        retry=3,
        save_last_try=False # 如果没False，每一次尝试的结果都会显示出来
    )

    runner.run(suite)