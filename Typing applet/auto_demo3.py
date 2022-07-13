from selenium import webdriver
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from ddt import ddt, data, unpack
import time

from util import Util

@ddt
class MMSLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://120.76.206.144:8080/mms/login.html"
        self.driver.implicitly_wait(5)
        self.imgs = []

    def tearDown(self) -> None:
        self.driver.quit()

    # @data(1,2,3)
    # def test_data(self, value):
    #     print(value)

    # def test_login_success(self):
    #     """
    #         当用户名和密码成功的时候，能够登录到系统当中
    #     :return:
    #     """
    #
    #     self.driver.get(self.url)
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     self.driver.find_element("id", "username").send_keys("admin")
    #     self.driver.find_element("id", "password").send_keys("123")
    #     self.driver.find_element("xpath", "//input[@value='Login']").click()
    #
    #     loginName = self.driver.find_element("id", "loginName").text
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #
    #     self.assertEqual(loginName, "adminxx")
    #

    # 参数化ddt进行不同参数测试同一个方法
    # @data(
    #     ("", "123", "User Id不能为空"),
    #     ("admin", "", "password不能为空"),
    #     ("adminx", "123", "没有此用户"),
    #     ("admin", "1234", "密码错误")
    # )
    # @data(*Util.get_data()) # 通过函数形式
    @data(*Util.get_data_from_file("datas.txt")) # 通过文件格式
    @unpack
    def test_login_fail(self, username, password, errmsg):
        """
            当用户名没有进行输入的时候，进行‘UserId不能为空’的弹框提示
        :return:
        """
        print(username, password, errmsg)
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element("id", "username").clear()  # 该操作是为了清空上一次输入未删除情况，避免造成下次联合记忆错误
        self.driver.find_element("id", "username").send_keys(username)
        time.sleep(1)
        self.driver.find_element("id", "password").clear()
        self.driver.find_element("id", "password").send_keys(password)
        time.sleep(1)
        self.driver.find_element("xpath", "//input[@value='Login']").click()
        time.sleep(1)

        errName = self.driver.find_element("xpath", "//div[contains(text(), '{}')]".format(errmsg)).text

        # self.imgs.append(self.driver.get_screenshot_as_base64())
        self.assertEqual(errmsg, errName)

        self.driver.find_element("xpath", "//span[contains(text(), '确定')]").click() # 提示框弹出点击确定，进行下一次测试




if __name__ == '__main__':
    # unittest.main()

    # HTMLTestRunner：优化界面形式的测试报告打出
    # logintestloader = unittest.defaultTestLoader.loadTestsFromTestCase(MMSLoginTest)
    # suite = unittest.TestSuite(logintestloader)
    #
    # runner = HTMLTestRunner(
    #     title = "带截图的测试报告",
    #     description = "xxx软件测试报告V1.0",
    #     stream=open("sample_test_report.html", "wb"),
    #     verbosity=2, # 详尽程度
    #     retry=3,
    #     save_last_try=False # 如果没False，每一次尝试的结果都会显示出来
    # )
    #
    # runner.run(suite)

    # 正常不带优化界面的方式进行测试
    login_loader = unittest.defaultTestLoader.loadTestsFromTestCase(MMSLoginTest)
    suite = unittest.TestSuite(login_loader)
    unittest.TextTestRunner().run(suite)