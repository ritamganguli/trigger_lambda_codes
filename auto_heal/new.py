import time
import os
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

print("Current working directory:", os.getcwd())

# Function to read data from Excel
