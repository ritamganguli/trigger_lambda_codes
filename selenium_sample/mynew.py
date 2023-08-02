from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://cgi-lib.berkeley.edu/ex/perl5/fup.html"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
# time.sleep(2)
# uname = driver.find_element("id","email")
# uname.send_keys("rakeshs@lambdatest.com")
time.sleep(12)