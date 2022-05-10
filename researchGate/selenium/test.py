import profile
from numpy import append
from selenium import webdriver
import time

def get_profile(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    profiles = []
    list = driver.find_elements_by_css_selector('.nova-legacy-e-text--size-l a')
    for i in list:
        profiles.append(i.get_attribute('href'))
    driver.close()
    return(profiles)

hust = 'https://www.researchgate.net/institution/Hanoi-University-of-Science-and-Technology/members'
total = []
for i in range(1,28):
    total.append(get_profile(hust+f'/{i}'))
