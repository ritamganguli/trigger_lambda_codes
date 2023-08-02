from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# import os
# url = "https://accounts.lambdatest.com/"




# options.browser_version = "112.0"
# options.platform_name = "Windows 11"

# capabilities = {
#         "build": "Build",
#         "name": "Test",
#         "platformName": "Windows 11",
#         "browserName": "Chrome",
#         "browserVersion": "latest",
#         "selenium_version": "3.9.1"
# }
# options = webdriver.ChromeOptions()
# options.browser_version = "112.0"
# options.platform_name = "Windows 11"
# lt_options = {}
# lt_options["username"] = "rakeshslambdatest"
# lt_options["accessKey"] = "MIBbYCQdJybdc0R0STUXKaZYt8XimqqH7lYBGi5hO2Rw0Oxjjw"
# lt_options["build"] = "Rakesh"
# lt_options["project"] = "Untitled"
# lt_options["console"] = "info"
#
# lt_options["selenium_version"] = "4.8.0"
# lt_options["w3c"] = True
# lt_options["plugin"] = "python-python"
# options.set_capability('LT:Options', lt_options)




options = webdriver.ChromeOptions()
options.browser_version = "112.0"
options.platform_name = "Windows 11"
lt_options = {}
lt_options["username"] = "rakeshslambdatest"
lt_options["accessKey"] = "MIBbYCQdJybdc0R0STUXKaZYt8XimqqH7lYBGi5hO2Rw0Oxjjw"
lt_options["visual"] = False
lt_options["video"] = True
lt_options["resolution"] = "2560x1440"
lt_options["network"] = True
lt_options["timezone"] = "Kolkata"
lt_options["project"] = "Untitled"
# lt_options["console"] = True
lt_options["console"] = "error"
# lt_options["tunnel"] = True
lt_options["geoLocation"] = "AU"
lt_options["terminal"] = True
lt_options["seTelemetryLogs"] = True
lt_options["networkThrottling"] = "Regular 4G"
lt_options["selenium_version"] = "4.8.0"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability('LT:Options', lt_options)


url = "https://hub.lambdatest.com/wd/hub"




driver = webdriver.Remote(
    command_executor=url,
    options=options
)




# driver = webdriver.Chrome()
driver.get("https://accounts.lambdatest.com/login")
# driver.maximize_window()
time.sleep(2)
uname = driver.find_element("id","email")
uname.send_keys("shubhamr@lambdatest.com")
# # driver.find_element()
# # time.sleep(2)
pswd = driver.find_element("id","password")
pswd.send_keys("Gmail@123")
# # time.sleep(2)
submit = driver.find_element("id","login-button")
submit.send_keys(Keys.ENTER)
time.sleep(5)

# # driver.find_element("id",).click();
# # driver.find_element("id","item__manage__team").click();
# # driver.find_element("id","profile__")
driver.find_element(By.XPATH,"//*[@id='profile__dropdown__parent']").click()
driver.find_element(By.XPATH,"//*[@id='item__manage__team']").click()
driver.find_element(By.XPATH,"//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]").click()
driver.find_element(By.XPATH,"//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]").click()
driver.get("https://cgi-lib.berkeley.edu/ex/perl5/fup.html")
time.sleep(2)
upload=driver.find_element(By.XPATH,"/html/body/form/input[1]")
# upload=driver.find_element(By.XPATH,"//input[@type='file']").click()
upload.send_keys("C:\\Users\\rakeshs\\Downloads\\Invited Users.csv")
save=driver.find_element(By.XPATH,"/html/body/form/input[3]")
save.click()
print("hello")

# dropdown=select(driver.find_element(By.ID,"profile__dropdown__parent"))
# dropdown.select_by_index(2).click();

# driver.find_element(By.ID,"item__manage__team").click()


time.sleep(30)

driver.quit()
