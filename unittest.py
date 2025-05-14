from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Şifre alanını bul
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")  
if(username_input=="tomsmith" & password_input=="SuperSecretPassword!"):
    pass
else:
    if(alert_input = driver.find_element(By.ID, "flash")):
        print("hata mesajı dönüyor.")



# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Kullanıcıdan input al
kullanici_adi = input("Kullanıcı adı: ")
sifre = input("Şifre: ")

# Input alanlarını bul ve değerleri gir
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys(kullanici_adi)
password_input.send_keys(sifre)

# Login butonuna tıkla
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Bekleyip uyarı mesajı çıkmış mı kontrol et
try:
    alert = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    print("Hata mesajı dönüyor:", alert.text)
except:
    print("Hata mesajı çıkmadı, giriş başarılı olabilir.")


