#encoding utf-8
import unittest
from macaca import WebDriver
from time import sleep


desired_caps = {
    'platformName': 'Desktop',  #// iOS, Android, Desktop
    'browserName': 'Chrome',    #// Chrome, Electron
}

server_url = {
    'hostname': '127.0.0.1', 
    'port': 3456
}

class MacacaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_url(self):
        self.driver.get('https://www.baidu.com')
        self.assertEqual(self.driver.title, 'baidu')

    # def test_search_macaca(self):
    #     self.driver.element_by_id("kw").send_keys("macaca")
    #     self.driver.element_by_id("su").click()
    #     sleep(2)
    #     title = self.driver.title
    #     self.assertTrue('macaca',title)


if __name__ == '__main__':
    unittest.main()


# import unittest
# from macaca import WebDriver

# desired_caps = {
# # iOS, Android, Desktop
#     'platformName': 'Desktop',
#     # Chrome, Electron 
#     'browserName': 'Chrome' 
#     # Only for mobile   
#     # 'app': 'path/to/app'       
# }

# server_url = {
#     'hostname': '127.0.0.1',
#     'port': 3456
# }

# class MacacaTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = WebDriver(desired_caps, server_url)
#         cls.driver.init()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     def test_get_url(self):
#         self.driver.get('https://www.google.com')
#         self.assertEqual(self.driver.title, 'Google')

#     def test_search_macaca(self):
#         self.driver.element_by_id("lst-ib").send_keys("macaca")
#         self.driver.element_by_name("btnK").click()
#         html = self.driver.source
#         self.assertTrue('macaca' in html)

# if __name__ == '__main__':
#     unittest.main()