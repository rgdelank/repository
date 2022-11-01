'''
Created on 31.10.2022

@author: mama
'''
from selenium import webdriver

class SeleniumDriver(object):
    '''
    classdocs
    '''
    browser = 'FireFox'
    driver = ""
        
    def __init__(self, params):
        '''
        Constructor
        '''
        self.main()
    
    def __del__(self):
        self.driver.quit()
        
    def main(self):
        
        if self.browser == 'FireFox':
    # Firefox
            from selenium.webdriver.firefox.service import Service
            firefox_driver_path_name = "D:\selenium\geckodriver.exe"
            firefox_browser_path_name = "C:\\Program Files\Mozilla Firefox\\firefox.exe"
            firefox_options = webdriver.FirefoxOptions
            firefox_options.binary = webdriver.FirefoxOptions.binary_location(firefox_browser_path_name)
            self.driver = webdriver.Firefox(service=Service(firefox_driver_path_name),options=firefox_options)

        elif self.browser == 'Chrom':
    # Chrome
            from selenium.webdriver.chrome.service import Service 
            chrom_browser_path_name   = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            chrom_driver_path_name   = "D:\selenium\chromedriver.exe"
            chrom_options = webdriver.ChromeOptions()
            chrom_options.binary_location = chrom_browser_path_name
            self.driver = webdriver.Chrome(service=Service(chrom_driver_path_name),options=chrom_options)

        elif self.browser == 'Edge':
    # Internet Explorer
            # Internet Explorer
            from selenium.webdriver.edge.service import Service 
            ie_driver_path_name      = "D:\selenium\msedgedriver.exe"
            ie_browser_path_name      = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            ie_options = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(service=Service(ie_driver_path_name),options=ie_options)

        else:
            print("Browser:" + self.browser + " is not supported.")
            exit(1)

