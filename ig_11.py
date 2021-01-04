from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

messenger = 'https://www.facebook.com/messages/t/100000021312021/'
driver.get(messenger)

username = '0970211299'
pw = 'Imoffline00'

driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(pw)
driver.find_element_by_name('pass').send_keys(Keys.ENTER)

message_field = driver.find_elements_by_class_name('_1mf _1mj')

message_field.send_keys('This is the first message sent by the bot!')
message_field.send_keys(Keys.ENTER)
