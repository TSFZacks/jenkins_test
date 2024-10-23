
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_chrome_driver():

    try:

        chrome_options = Options()

        driver = webdriver.Chrome(options=chrome_options)

        return driver
    
    except Exception:

        return None

def main(driver):

    driver.get('https://www.youtube.com')
    time.sleep(10)

    pesquisa_input = driver.find_element(By.XPATH, '//a[@title="Shorts"]')
    pesquisa_input.click()
    time.sleep(10)
    """like = driver.find_elements(By.XPATH, "//span[contains(text(), 'mil')]")
    like[0].click()
    time.sleep(1000)
    """
driver = open_chrome_driver()
main(driver)