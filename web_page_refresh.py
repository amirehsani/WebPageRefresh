from selenium import webdriver
import time

refresh_rate = 20
url_buffer = input("Enter your URL: ")

driver = webdriver.Firefox()
driver.get('https://' + url_buffer)

for i in range(5):
	time.sleep(refresh_rate)
	driver.refresh()