import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, value= "Login").click()
        time.sleep(1)
        driver.find_element(By.ID, "Username").send_keys("dfebri")
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys("Azura#01")
        time.sleep(1)
        driver.find_element(By.NAME, value= "login").click()
        time.sleep(5)
        driver.find_element(By.NAME, "searching").send_keys("Test Baca")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(2)").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".btn-outline-info").click()
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, ".btn-link").click()
        time.sleep(3)

unittest.main()