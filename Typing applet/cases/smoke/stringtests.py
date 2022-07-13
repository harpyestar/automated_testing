import unittest


class StringTest(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def testSmokeStr1(self):
        self.assertIn("hello", "hello world")

    def testSmokeStr2(self):
        self.assertNotIn("hello", "hello 12")

