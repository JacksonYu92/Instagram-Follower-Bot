from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


chrome_driver_path = "C:\Development\chromedriver.exe"

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        time.sleep(2)
        fb_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]')
        fb_login.click()

        time.sleep(2)
        fb_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_input.send_keys(USERNAME)
        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_input.send_keys(PASSWORD)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        time.sleep(5)
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]'))).click()
        # notification_later_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        # notification_later_btn.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        followers_popup = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            time.sleep(2)



    def follow(self):
        buttons = self.driver.find_elements_by_css_selector("li button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

instafollower = InstaFollower(chrome_driver_path)
instafollower.login()
instafollower.find_followers()
instafollower.follow()