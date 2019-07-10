# from appium import webdriver
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.2'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
from time import sleep
import os

# success = True
# desired_caps = {}
# desired_caps['appium-version'] = '1.0'
# desired_caps['platformName'] = 'iOS'
# desired_caps['platformVersion'] = '9.2'
# desired_caps['deviceName'] = 'iPhone 5'
# desired_caps['app'] = os.path.abspath('/Users/zhu/Downloads/DailyCast.app')

# wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
# wd.implicitly_wait(30)



# try:
# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]").click()
# 	wd.implicitly_wait(200)

# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[2]").click()
# 	wd.implicitly_wait(50)

# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[1]").click()
# 	wd.implicitly_wait(50)
# finally:
# 	wd.quit()


###############android

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.1'
desired_caps['deviceName'] = 'LG-D858'
desired_caps['app'] = os.path.abspath('/Users/zhu/Downloads/dailycast-plus-debug-v3.0.18-238.apk')
desired_caps['appPackage'] = 'com.suapp.dailycast'

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	# wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]").click()
	# sleep(10)
	for i in range(5):
		print i
		wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.view.View[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]").click()
		sleep(10)
		wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.view.View[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]").click()
		sleep(10)
		wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[2]").click()
		sleep(1)
		wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[1]").click()
		sleep(1)
		wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.view.View[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")


