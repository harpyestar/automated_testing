from selenium import webdriver
import unittest
import time



class MMSLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://120.76.206.144:8080/mms/login.html"
        self.driver.implicitly_wait(5)
        self.imgs = []

    def addpic(func):
        def wrapper(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except AssertionError as e:
                import os, time
                day = time.strftime("%Y%m%d", time.localtime(time.time()))
                screenshot_path = os.getcwd() + r"\reports\screenshot_%s" % day
                if not os.path.exists(screenshot_path):
                    os.makedirs(screenshot_path)

                tm = time.strftime("%H%M%S", time.localtime(time.time()))
                self.driver.get_screenshot_as_file(screenshot_path + "\\{}_{}.png".format("screen_shot", tm))
                raise e     #将异常继续抛出给unittest，必须要写

        return wrapper

    @addpic
    def test_demo1(self):
        self.driver.get(self.url)
        self.assertEqual(1,1)




if __name__ == '__main__':
    # 正常不带优化界面的方式进行测试
    login_loader = unittest.defaultTestLoader.loadTestsFromTestCase(MMSLoginTest)
    suite = unittest.TestSuite(login_loader)
    unittest.TextTestRunner().run(suite)