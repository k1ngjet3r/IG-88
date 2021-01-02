from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/Jeter/Downloads/chromedriver')

messenger = 'https://www.facebook.com/messages/t/100000021312021/'
driver.get(messenger)

username = '0970211299'
pw = 'Imoffline00'

driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(pw)
driver.find_element_by_name('pass').send_keys(Keys.ENTER)

message_field = driver.find_elements_by_xpath(
    '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')

message_field.send_keys('This is the first message sent by the bot!')
message_field.send_keys(Keys.ENTER)
