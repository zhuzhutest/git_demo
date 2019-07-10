#-*-coding:utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
import time
import os
success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.2'
desired_caps['deviceName'] = 'iPhone 6s'
desired_caps['app'] = 'com.sube.dailycast'
# desired_caps['app'] = os.path.abspath('/Users/zhu/Downloads/DailyCast.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
# wd.implicitly_wait()

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False
try:
	
	# 启动引导页点击get按钮 
# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click
#   # sign in 
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click
	el = wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]").get_attribute('value')
	print el
	if "Sign in to upgrade level for more fun" == str(el):
		print "ok"
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click	
# 	# 点击feed第一个cell
# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()
# 	# 等待30秒
# 	wd.implicitly_wait(30)
# 	# 点击视频播放页面的关闭按钮
# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
# 	wd.implicitly_wait(30)
# 	# 点击视频的tag
# 	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]").click()
# 	wd.implicitly_wait(30)

finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")
