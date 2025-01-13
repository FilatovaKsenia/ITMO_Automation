from selenium import webdriver
from selenium.webdriver.common.by import By

def find_on_page():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')


    field_1 = driver.find_element(By.CSS_SELECTOR, '#user-name')
    if field_1 is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

    field_2 = driver.find_element(By.CSS_SELECTOR, '#password')
    if field_2 is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

    btn = driver.find_element(By.CSS_SELECTOR, '#login-button')
    if btn is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

find_on_page()



