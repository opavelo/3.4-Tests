import unittest
from main import Yandex

yd = Yandex('YD Token')

class TestSomething(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def test_response(self):
        self.assertEqual(str(yd.yd_folder_create('Name2')), '<Response [409]>')

    def test_folder_appearence(self):
        self.assertIn('Name2', yd.checking_avaliability())

    def tearDown(self):
        print('method tearDown')

if __name__ == '__main__':
    unittest.main()