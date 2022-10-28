from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

username="" # username 
password="" # password

class Github:

    chrome_driver_path="" # chrome driver path => (C:/Users/xxx/xxx/Desktop/chromedriver)

    def __init__(self):
        self.browser=webdriver.Chrome(executable_path=Github.chrome_driver_path)
        self.url=("https://github.com/")
        self.username= username
        self.password= password
        self.followers=[]

    def signIn(self):
        self.browser.get(self.url+"login")
        self.browser.find_element(By.NAME,'login').send_keys(self.username)
        self.browser.find_element(By.NAME,'password').send_keys(self.password)
        self.browser.find_element(By.NAME,'commit').click()
        time.sleep(2)
    
    def get_profile(self):
        self.browser.get(self.url +'Er00t') # your profile name
        

        
app=Github() # open githup page
app.signIn() # sign in github
app.get_profile() # Open your profile