import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# Function to read data from Excel
def read_excel_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data_list = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data_list.append({
            "username": row[0],
            "access_key": row[1],
        })
    return data_list

# Path to the Excel file and sheet name
file_path = "./home/vsts/work/1/s/auto_heal/Sheet1.xlsx"
sheet_name = "Sheet1"

# Read data from Excel
excel_data_list = read_excel_data(file_path, sheet_name)

grid_url = "hub.lambdatest.com/wd/hub"

lt_options_base = {
    "project": "Parallel1",
    "selenium_version": "4.0.0",
    "w3c": True,
}

for excel_data in excel_data_list:
    username = excel_data["username"]
    access_key = excel_data["access_key"]

    lt_options = lt_options_base.copy()
    lt_options["username"] = username
    lt_options["accessKey"] = access_key

    desired_capabilities_1= {
        "platformName": "Windows 11",
        "browserName": "Chrome",
        "browserVersion": "",
        "name": "My Test Name",
        "build": "Selenium Sample",
        "network": True,
        "visual": True,
        "video": True,
        "console": True,
        "tunnel": False,
        "LT:Options": lt_options,
    }

    driver = webdriver.Remote(
        command_executor=f"https://{grid_url}",
        desired_capabilities=desired_capabilities_1
    )

    try:
        driver.get("https://accounts.lambdatest.com/")
        u_name = driver.find_element("id", "email")
        u_name.send_keys(username)

        p_word = driver.find_element("id", "password")
        p_word.send_keys(access_key)

        time.sleep(10)
        # Additional code for your test goes here

    except TimeoutException as e:
        print(f"Exception occurred: {e}")

    finally:
        # Quit the driver regardless of the exception
        driver.quit()
