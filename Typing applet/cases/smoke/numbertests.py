import unittest


class NumTest(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def testSmokeNum1(self):
        self.assertEqual(1,1)

    def testSmokeNum2(self):
        self.assertNotEqual(1,1)

