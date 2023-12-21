from instagram_private_api import Client
from instagram_private_api.errors import ClientError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Evite hardcoding de credenciais
username = input("Insira seu nome de usuário do Instagram: ")
password = input("Insira sua senha do Instagram: ")

perfil_privado = ' '  # colocar o nome do usuário

# Instancia um objeto do tipo webdriver do navegador Chrome
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Abre a página do Instagram com o comando do web drive
driver.get('https://www.instagram.com/accounts/login/')

# Espera até que o campo de username esteja presente
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
username_field.send_keys(username)

# Espera até que o campo de password esteja presente
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)
password_field.send_keys(password)

# Pressiona a tecla enter automaticamente para fazer o login
password_field.send_keys(Keys.RETURN)

# Espera até que o usuário faça a autenticação
WebDriverWait(driver, 40).until(
    EC.url_contains('instagram.com')
)

try:
    api = Client(username, password)
    user_info = api.username_info(perfil_privado)
    user_id = user_info['user']['pk']
    feed = api.user_feed(user_id)

    for post in feed.get('items', []):
        print(post)
        time.sleep(5)

    # Continua a rodar essa caralha de onde parou
    for post in feed.get('items', []):
        print(post)
        time.sleep(5)

except ClientError as e:
    print(f"Ocorreu um erro: {e.msg}")

finally:
    # Fecha o navegador automaticamente
    driver.quit()
