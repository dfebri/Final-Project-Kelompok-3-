from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class dashboard(unittest.TestCase):

    def set_dashboard(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_dashboard_home(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()

        self.driver.find_element(By.LINK_TEXT, "Home").click()
        self.driver.find_element(By.CSS_SELECTOR, "body > div > div.jumbotron > p:nth-child(4) > a").click()          
        time.sleep(2)

    def test_dashboard_practice(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()

        self.driver.find_element(By.LINK_TEXT, "Practice").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p/button").click()    
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/p/button").click() 
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/p/button").click()    
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/p/button").click()      
        time.sleep(2)

    def test_dashboard_testautomation(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()

        self.driver.find_element(By.LINK_TEXT, "Test Automation").click()
        self.driver.find_element(By.ID, "name").send_keys("Cahyo")
        self.driver.find_element(By.ID, "phone").send_keys("082220822220 ")
        self.driver.find_element(By.ID, "email").send_keys("dwifebrimurcahyo@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Test01")
        self.driver.find_element(By.ID, "address").send_keys("Kabupaten Karawang")
        self.driver.find_element(By.ID, "phone").send_keys("082220822220")
        self.driver.find_element(By.NAME, "submit").click()   
        self.driver.find_element(By.ID, "male").click()
        self.driver.find_element(By.ID, "monday").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div/select").click()    
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[1]/div[1]/label").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div[1]/label").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/div/div[1]/label").click()
        time.sleep(2)

    def test_dashboard_tutorial(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()

        self.driver.find_element(By.LINK_TEXT, "Tutorial").click()    
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
