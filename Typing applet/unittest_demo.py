import unittest

class Demo(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("setUpClass")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("tearDownClass")
    #
    # def setUp(self):
    #     print("init")
    #
    # def tearDown(self):
    #     print("end")

    def testFun(self):
        print("test_way")

    def testAFun2(self): # 字母序或数字序，test开头一定要有
        print("test_way2")

# demo = Demo()

if __name__ == '__main__':
    print("测试开始咯")
    unittest.main()