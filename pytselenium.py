#Bu program sahibinden.com üzerinden aratmak istediğin kelime ile ilgili kaç adet sonuç bulunduğunu ekrana yazdırıyor.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
class Twitter:
    def __init__(self):
        self.browserProfile=webdriver.ChromeOptions()
        self.carn=carsname
        self.browser=webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        
    def singIn(self):
        self.browser.get('https://www.sahibinden.com/')
        
        usern=self.browser.find_element(By.XPATH,'//*[@id="searchText"]')
        
        time.sleep(3)
        usern.send_keys(self.carn)
        time.sleep(3)
        usern.send_keys(Keys.ENTER)
        time.sleep(3)
        number=self.browser.find_element(By.XPATH,'//*[@id="wideContainer"]/div/div[1]/h1/span/span/strong')
        print("\n\n\n\t\tArattığınız "+self.carn+" marka ile alakalı toplam "+number.text+" sonuç bulunuyor.")
        
carsname=input("\n\n\t\tAramak istediğiniz kelime:")
twitter= Twitter()
twitter.singIn()

        