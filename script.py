from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def open_chrome_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')  # Rodar sem interface gráfica
        chrome_options.add_argument('--disable-dev-shm-usage')

        chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

        # Configurar o caminho do Chromedriver
        service = Service('/opt/chromedriver/chromedriver-linux64/chromedriver')

        # Inicializar o WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        return driver

    except Exception as e:
        print(f"Erro ao abrir o Chrome: {e}")
        return None

def lambda_handler():
    driver = open_chrome_driver()
    driver.get('https://www.youtube.com')
    time.sleep(10)
    print(driver.current_url)
    time.sleep(10)
    ######