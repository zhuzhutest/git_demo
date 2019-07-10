import unittest
import time
import threading
from macaca import WebDriver

desired_caps = {
				'platformName': "Desktop",	#// iOS, Android, Desktop
				'browserName': "Electron",		#// Chrome, Electron
			}

server_url = {
		'hostname': '127.0.0.1',
		'port': 3456
		}
class MacacaTest(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.driver = WebDriver(desired_caps, server_url)
		self.driver.init()
		self.driver.maximize_window()
		self.driver.get('http://w.url.cn/s/Au4fnTO')
		time.sleep(1)
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()
	def test_open(self):
		for i in xrange(100):
			self.driver.refresh()
			time.sleep(4)

if __name__ == '__main__':
	unittest.main()