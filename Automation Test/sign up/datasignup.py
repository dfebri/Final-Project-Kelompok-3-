import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
   
def Positive(driver):
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Sign Up").click()
    time.sleep(3)
    driver.find_element(By.ID,'FirstName').send_keys('1')
    driver.find_element(By.ID,'Surname').send_keys('1')
    driver.find_element(By.ID,'E_post').send_keys('1')
    driver.find_element(By.ID,'Mobile').send_keys('1')
    driver.find_element(By.ID,'Username').send_keys('ma')
    driver.find_element(By.ID,'Password').send_keys('1')
    driver.find_element(By.ID,'ConfirmPassword').send_keys('1')

def Negative1(driver): #Username already exist
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Sign Up").click()
    time.sleep(3)
    driver.find_element(By.ID,'FirstName').send_keys('1')
    driver.find_element(By.ID,'Surname').send_keys('1')
    driver.find_element(By.ID,'E_post').send_keys('1')
    driver.find_element(By.ID,'Mobile').send_keys('1')
    driver.find_element(By.ID,'Username').send_keys('16')
    driver.find_element(By.ID,'Password').send_keys('1')
    driver.find_element(By.ID,'ConfirmPassword').send_keys('1')

def Negative2(driver): #Not input surname
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Sign Up").click()
    time.sleep(3)
    driver.find_element(By.ID,'FirstName').send_keys('1')
    driver.find_element(By.ID,'E_post').send_keys('1')
    driver.find_element(By.ID,'Mobile').send_keys('1')
    driver.find_element(By.ID,'Password').send_keys('1')
    driver.find_element(By.ID,'ConfirmPassword').send_keys('1')

def Negative3(driver): #Not input firstname
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Sign Up").click()
    time.sleep(3)
    driver.find_element(By.ID,'Surname').send_keys('1')
    driver.find_element(By.ID,'E_post').send_keys('1')
    driver.find_element(By.ID,'Mobile').send_keys('1')
    driver.find_element(By.ID,'Username').send_keys('16')
    driver.find_element(By.ID,'Password').send_keys('1')
    driver.find_element(By.ID,'ConfirmPassword').send_keys('1')
        
def Negative4(driver): #Not input username
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Sign Up").click()
        time.sleep(3)
        driver.find_element(By.ID,'FirstName').send_keys('1')
        driver.find_element(By.ID,'Surname').send_keys('1')
        driver.find_element(By.ID,'E_post').send_keys('1')
        driver.find_element(By.ID,'Mobile').send_keys('1')

def Negative5(driver): #Not input password
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Sign Up").click()
    time.sleep(3)
    driver.find_element(By.ID,'FirstName').send_keys('1')
    driver.find_element(By.ID,'Surname').send_keys('1')
    driver.find_element(By.ID,'E_post').send_keys('1')
    driver.find_element(By.ID,'Mobile').send_keys('1')
    driver.find_element(By.ID,'Username').send_keys('16')   

def Negative6(driver): #Confirm password and password not match
    driver.get("https://itera-qa.azurewebsites.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Sign Up").click()
    time.sleep(3)
    driver.find_element(By.ID,'FirstName').send_keys('1')
    driver.find_element(By.ID,'Surname').send_keys('1')
    driver.find_element(By.ID,'E_post').send_keys('1')
    driver.find_element(By.ID,'Mobile').send_keys('1')
    driver.find_element(By.ID,'Username').send_keys('888')
    driver.find_element(By.ID,'Password').send_keys('1')
    driver.find_element(By.ID,'ConfirmPassword').send_keys('2')