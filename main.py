from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Initialize browser with webdriver and wait 5 seconds
browser = webdriver.Firefox()
browser.implicitly_wait(5)

#Use browser to get HTTPS link
browser.get('https://www.instagram.com/')

#Sleep for 2 seconds to let page load
sleep(2)

#Look for username and password elements
username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

#Input selected username and password
username_input.send_keys("terracottatoy")
password_input.send_keys("ouroboros")

#Click the login button
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()