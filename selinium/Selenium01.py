#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://dominos.com")

time.sleep(3)

click_sign_in = driver.find_element_by_xpath('//*[@id="_dpz"]/header/nav[1]/div[1]/div[3]')

click_sign_in.click()

time.sleep(3)
idemail = driver.find_element_by_name("Email")
idemail.click()
idemail.send_keys("scott.l.sievers@verizon.com")

time.sleep(1)
idpassword = driver.find_element_by_id("Password")
idpassword.click()
idpassword.send_keys("PASSWORD")
idpassword.send_keys(Keys.RETURN)
