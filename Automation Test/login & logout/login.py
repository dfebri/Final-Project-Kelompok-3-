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

    def test_Login_Negatif1(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs login
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("nadya") # isi username valid
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("pwsalah1") # isi password salah
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)
        
        response_message = driver.find_element(By.CLASS_NAME,"alert-danger") 

    def test_Login_Negatif2(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("akunsalah") # isi username salah
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456.") # isi password valid
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)
        
        response_message = driver.find_element(By.CLASS_NAME,"alert-danger") 

    def test_Login_Negatif3(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("") # kosongkan username 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("") # kosongkan password
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)
        
        response_message = driver.find_element(By.CLASS_NAME,"alert-danger") 

    def test_Login_Negatif4(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("nadya") # isi username valid
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("") # kosongkan password 
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)
        
        response_message = driver.find_element(By.CLASS_NAME,"alert-danger") 

    def test_Login_Negatif5(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("") # kosongkan username 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456.") # isi password valid
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)
        
        response_message = driver.find_element(By.CLASS_NAME,"alert-danger") 

    def test_Login_Positif1(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Login").click() #click login text
        driver.find_element(By.ID,"Username").send_keys("nadya") # isi username valid
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456.") # isi password valid
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()


    def test_Login_Positif2(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Login").click() #click login text
        driver.find_element(By.ID,"Username").send_keys("NADYA") # isi username dengan huruf kapital
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456.") # isi password valid
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)

    def test_Login_Positif3(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/login") # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Login").click() #click login text
        driver.find_element(By.ID,"Username").send_keys("Nadya") # isi username dengan huruf kapital di awal
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456.") # isi password valid
        time.sleep(1)
        driver.find_element(By.NAME,value="login").click()
        time.sleep(1)
     
unittest.main()