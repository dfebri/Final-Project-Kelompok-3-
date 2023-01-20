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
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Login").click() #click login text
        driver.find_element(By.ID,"Username").send_keys("nadya") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456.") # isi password
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Log out").click() #click logout text
        time.sleep(3)

     
unittest.main()