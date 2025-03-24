import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'que acesso o site advantageonlineshopping')
def step_impl(context):
    context.driver = webdriver.Chrome()     
    context.driver.maximize_window()        
    context.driver.implicitly_wait(12)      
    context.driver.get("https://www.advantageonlineshopping.com/#/")
    context.driver.implicitly_wait(10)
      
@when(u'acesso a pagina de cadastro')
def step_impl(context):
    context.driver.find_element(By.ID,"menuUser").click()
    time.sleep(10)
    context.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").click()

@then(u'preencho os dados de cadastro com Username {Username} Password {Password} Email {Email} Confirmpassword {Confirmpassword}')
def step_impl(context, Username, Password, Email, Confirmpassword ):
    context.driver.find_element(By.NAME,"usernameRegisterPage").click()
    context.driver.find_element(By.NAME,"usernameRegisterPage").send_keys(Username)
    context.driver.find_element(By.NAME,"passwordRegisterPage").click()
    context.driver.find_element(By.NAME,"passwordRegisterPage").send_keys(Password)
    context.driver.find_element(By.NAME,"emailRegisterPage").click()
    context.driver.find_element(By.NAME,"emailRegisterPage").send_keys(Email)
    context.driver.find_element(By.NAME,"confirm_passwordRegisterPage").click()
    context.driver.find_element(By.NAME,"confirm_passwordRegisterPage").send_keys(Confirmpassword)
    
@then(u'aceito os termos de privacidade e clico no botão registrar')
def step_impl(context):
    context.driver.find_element(By.NAME,"i_agree").click()
    context.driver.find_element(By.ID,"register_btn").click()

@when(u'acesso a pagina de login')
def step_impl(context):
    context.driver.find_element(By.ID,"menuUser").click()
    time.sleep(5) 
#.......................................................................................................................

@when(u'preencho os campos de login com Username {Username} e Password {Password}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  
    context.driver.find_element(By.ID, "password").send_keys(senha)  
    time.sleep(10)   
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(10) 

@when(u'estou na pagina home clico no banner de Tablets')
def step_impl(context):
    context.driver.find_element(By.ID, "tabletsImg").click()
    time.sleep(10) 
    
@then(u'valido se estou na página de Tablets')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".categoryTitle").text == "TABLETS"
    time.sleep(10) 
    
@when(u'seleciono o produto "HP ELITEPAD 1000 G2 TABLET"')
def step_impl(context):
    context.driver.find_element(By.ID, "16").click()
    time.sleep(10) 
    
@then(u'valido o nome do produto e o valor')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".screen768:nth-child(1)").text == "HP ELITEPAD 1000 G2 TABLET"
    context.driver.find_element(By.CSS_SELECTOR, ".screen768:nth-child(2)").text == "$1,009.00"
    time.sleep(10) 

@when(u'adiciono o produto "HP ELITEPAD 1000 G2 TABLET" ao carrinho de compras')
def step_impl(context):
    context.driver.find_element(By.NAME, "save_to_cart").click()
    time.sleep(10) 
    
@then(u'valido se estou no carrinho de compras e a quantidade adicionada')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#menuCart > path").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".sticky").text == "SHOPPING CART (1)"
    time.sleep(10) 

@then(u'removo o produto "HP ELITEPAD 1000 G2 TABLET" do carrinho de compras')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "REMOVE").click()
    time.sleep(10)

@then(u'acesso o menu faço o logout')
def step_impl(context):
    context.driver.find_element(By.ID, "menuUser").click()
    context.driver.find_element(By.CSS_SELECTOR, ".roboto-medium:nth-child(3)").click()
    context.driver.quit()

#.......................................................................................................................
    
@then(u'preencho os campos de login com Username {Username} e Password {Password}')
def step_impl(context, Username, Password):
    context.driver.find_element(By.NAME,"username").click()
    context.driver.find_element(By.NAME,"username").send_keys(Username)
    context.driver.find_element(By.NAME,"password").click()
    context.driver.find_element(By.NAME,"password").send_keys(Password)
    context.driver.find_element(By.ID,"sign_in_btn").click()
    time.sleep(5)

@then(u'exibe a {mensagem} de erro quando o login não é o correto')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.ID, "signInResultMessage").text == mensagem
    context.driver.quit()
 