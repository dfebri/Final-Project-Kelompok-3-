import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import dataSignUp

class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Sign_Up_Positive(self):
        driver = self.driver
        dataSignUp.Positive(driver)
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.CLASS_NAME,'label-success').text
        self.assertEqual(response_message, 'Registration Successful')

    def test_Sign_Up_Negative1(self): #User has already exist
        driver = self.driver
        dataSignUp.Negative1(driver)
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.CLASS_NAME,'label-danger').text
        self.assertEqual(response_message, 'Username already exist')

    def test_Sign_Up_Negative2(self): #Not input surname
        driver = self.driver
        dataSignUp.Negative2(driver)
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.ID,'Surname-error').text
        self.assertEqual(response_message, 'Please enter surname')

    def test_Sign_Up_Negative3(self): #Not input firstname
        driver = self.driver
        dataSignUp.Negative3(driver)
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.ID,'FirstName-error').text
        self.assertEqual(response_message, 'Please enter first name')
    
    def test_Sign_Up_Negative4(self): #Not input username
        driver = self.driver
        dataSignUp.Negative4(driver) 
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.ID,'Username-error').text
        self.assertEqual(response_message, 'Please enter username')
    
    def test_Sign_Up_Negative5(self): #Not input password
        driver = self.driver
        dataSignUp.Negative5(driver)
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.ID,'Password-error').text
        self.assertEqual(response_message, 'Please enter password')

    def test_Sign_Up_Negative6(self): #Confirm password and password not match
        driver = self.driver
        dataSignUp.Negative6(driver)
        driver.find_element(By.ID,'submit').click()

        response_message = driver.find_element(By.ID,'ConfirmPassword-error').text
        self.assertEqual(response_message, "'Confirm password' and 'Password' do not match.")

unittest.main()