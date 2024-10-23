from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_chrome_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')  # Rodar sem interface gráfica
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Caminho atualizado do ChromeDriver
        driver = webdriver.Chrome(executable_path='/var/lib/jenkins/chromedriver/chromedriver', options=chrome_options)

        return driver
    
    except Exception as e:
        print(f"Erro ao abrir o Chrome: {e}")
        return None

def main(driver):
    driver.get('https://www.youtube.com')
    time.sleep(10)

    pesquisa_input = driver.find_element(By.XPATH, '//a[@title="Shorts"]')
    pesquisa_input.click()
    time.sleep(10)

driver = open_chrome_driver()
if driver:
    main(driver)
    driver.quit()
