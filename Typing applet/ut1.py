import unittest, os

base_dir = os.path.dirname(os.path.abspath(__file__))  # 第二种，该代码存放的根目录

if __name__ == '__main__':

    case_dir = '/cases'
    dis = unittest.defaultTestLoader.discover(base_dir+case_dir+'/smoke', pattern="*.py")
    suite = unittest.TestSuite(dis)
    unittest.TextTestRunner().run(suite)


