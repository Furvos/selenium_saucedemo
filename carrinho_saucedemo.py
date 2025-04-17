from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def automatizar_saucedemo():

    chrome_options = Options()
    # sem interface gráfica (headless):
    # chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        
        print("Abrindo o site...")
        driver.get("https://www.saucedemo.com/")
        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        
        print("Realizando login...")
        username_field.send_keys("standard_user") 
        # standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce") # só tem essa senha msm
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        # verificar se o login foi bem-sucedido aguardando um elemento da página de produtos
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        print("Login realizado com sucesso!")
        
        print("Adicionando produto ao carrinho...")
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart')]")
        produto_nome = driver.find_element(By.XPATH, "//div[contains(@class, 'inventory_item_name')]").text
        add_to_cart_button.click()
        
        # verificar se o produto foi adicionado ao carrinho
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        if cart_badge.text == "1":
            print(f"Produto '{produto_nome}' adicionado ao carrinho com sucesso!")
        
        # abrir o carrinho para verificação
        cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        print("Carrinho aberto e produto verificado!")
        
        time.sleep(10)
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    finally:
        print("Finalizando automação...")
        driver.quit()

if __name__ == "__main__":
    automatizar_saucedemo()