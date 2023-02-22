from instagram_private_api import Client
from instagram_private_api.errors import ClientError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# colocar o usuário para inserir o login e a senha ou eu posso já definir automaticamente
#Para definir automaticamente tirar

username = input("Insira seu nome de usuário do Instagram: ")
password = input("Insira sua senha do Instagram: ")

perfil_privado = ' ' #colocar o nome do usuário

# Instancia um objeto do tipo webdriver do navegador, ou seja, Esse trecho de código instancia um objeto do tipo webdriver do navegador Chrome utilizando o chromedriver.exe como serviço. O webdriver é uma ferramenta que permite interagir com um navegador de forma automatizada através de código Python. Já o chromedriver.exe é um executável que fornece a interface entre o webdriver e o navegador Chrome. Ao instanciar um objeto webdriver.Chrome, o programa abre uma janela do navegador Chrome e a partir daí é possível controlar as ações do navegador (navegar para uma página, preencher campos, clicar em botões etc.) através do objeto driver.

# Em programação, uma instância é um objeto criado a partir de uma classe. A classe define a estrutura e comportamento do objeto, enquanto a instância é uma cópia dessa estrutura em tempo de execução, com seus próprios valores únicos para cada atributo. Em outras palavras, uma instância é uma versão específica de uma classe que pode ser manipulada e utilizada pelo programa. Por exemplo, se você tiver uma classe "Carro", uma instância seria um carro específico, com sua própria cor, modelo, ano e outras características únicas.


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Abre a página do Instagram com o comando do web drive
driver.get('https://www.instagram.com/accounts/login/')

# Espera a página carregar
sleep(3)

# Encontra o campo de username na pagina e coloca o login
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys(username)

# Encontra o campo de password e coloca a senha
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(password)

# Pressiona a tecla enter automaticamente pra fazer o login
password_field.send_keys(Keys.RETURN)

# Espera para o usuario fazer a autenticação
sleep(40)

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

# Fecha o navegador automaticamente
driver.quit()