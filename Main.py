'''
Created on 31.10.2022

@author: Roberto 
'''
# Import all necesary files for the whole Enterprise Tests application.
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from EnterpriseTests.SeleniumDriver import SeleniumDriver 
from pickle import NONE

class Main():
    def run(self):
        sdrv = SeleniumDriver().driver

        sdrv.implicitly_wait(30)
        sdrv.maximize_window()

#navigate to the application home page
#driver.delete_all_cookies()
        sdrv.get("https://pcmama/")
        sdrv.fullscreen_window()

        element = sdrv.find_element(By.XPATH ,"//input[@name='phrase']")
        element.clear()
        element.send_keys('selenium test')

        element = sdrv.find_element(By.XPATH ,"//input[@name='letters']")
        element.clear()
        element.send_keys('aeiou')

        element = sdrv.find_element(By.XPATH ,"//input[@value='Los geht']")
        element.click()

        sdrv.get("https://pcmama/tabla")
        sdrv.fullscreen_window()

#close the browser window
        time.sleep(10)

        sdrv = None
        
if __name__ == '__main__':
    MyMain = Main()
    Main.run()