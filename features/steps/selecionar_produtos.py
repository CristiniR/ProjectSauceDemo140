import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que entro no site Sauce Demo')
@given(u'que acesso o site Sauce Demo')
def step_impl(context):

    context.driver = webdriver.Chrome()     
    context.driver.maximize_window()        
    context.driver.implicitly_wait(10)      
    context.driver.get("https://www.saucedemo.com") 


@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  
    context.driver.find_element(By.ID, "password").send_keys(senha)     
    context.driver.find_element(By.ID, "login-button").click()     

@then(u'valido se estou na página de Produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"  

@when(u'adiciono o produto "Sauce Labs Backpack" ao carrinho de compras')
def step_impl(context):
    context.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() 
    
@then(u'valido a quantidade do carrinho de compras')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1"

@when(u'acesso o carrinho de compras')
def step_impl(context):
   context.driver.find_element(By.ID,"shopping_cart_container").click() 

@then(u'valido se o nome do produto no carrinho é "Sauce Labs Backpack" e se o preço do produto no carrinho é "$29.99"')
def step_impl(context):
   assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"
   assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"

@then(u'removo o produto "Sauce Labs Backpack" do carrinho de compras')
def step_impl(context):
   context.driver.find_element(By.ID,"remove-sauce-labs-backpack").click()

@when(u'acesso o menu faço o logout')
def step_impl(context):
   context.driver.find_element(By.ID,"react-burger-menu-btn").click()
   context.driver.find_element(By.ID,"logout_sidebar_link").click()
   context.driver.quit()

@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
   
    context.driver.find_element(By.ID, "password").send_keys(senha)     
    context.driver.find_element(By.ID, "login-button").click()         


@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  
    context.driver.find_element(By.ID, "login-button").click()          


@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()          


# Preencher com usuário e senha através da decisão (IF)..........................................................................
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
        # se o usuário estiver em <branco> não há ação de preenchimento

    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
        # se a senha estiver em <branco> não há ação de preenchimento

    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    # time.sleep(2) # espera por 2 segundos - remover depois = alfinete

    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
   # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento
    context.driver.quit()


# Verifica a mensagem para o Scenario Outline..........................................................................................
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem
    context.driver.quit()

