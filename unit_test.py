from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Giriş bilgilerini gir
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("tomsm")
password_input.send_keys("SuperSecretPassword!")

# Giriş butonuna tıkla
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


try:
    WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))    )
    print("Basarili giris mesaji ekrana yaziliyor")
except:
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error"))    )
    print("Hatali giris mesaji ekrana yaziliyor")

driver.quit()

