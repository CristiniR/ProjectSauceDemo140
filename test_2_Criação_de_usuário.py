import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_2_Criação_de_usuário():

    url = "https://www.agromeyer.com.br/"                 


    def setup_method(self, method):                  
        self.driver = webdriver.Chrome()              
        self.driver.implicitly_wait(15)               

    def teardown_method(self, method):                
        self.driver.quit()              

    # Criação de Usuário---------------------------------------------------------------------------------------------------
        
    def test_selecionar_produto(self):   
            self.driver.get(self.url)             
            self.driver.find_element(By.CSS_SELECTOR, ".item-menu-descricao:nth-child(3) > strong:nth-child(2)").click()
            self.driver.find_element(By.ID, "register-button").click()
            self.driver.find_element(By.ID, "pf_nome_cliente").click()
            self.driver.find_element(By.ID, "pf_nome_cliente").send_keys("Débora Milena Fernandes") 
            self.driver.find_element(By.ID, "pf_cpf_cliente").click()
            self.driver.find_element(By.ID, "pf_cpf_cliente").send_keys("654.133.357-25")
            self.driver.find_element(By.ID, "telefone_cliente").click()
            self.driver.find_element(By.ID, "telefone_cliente").send_keys("(48)3881-9047")
            self.driver.find_element(By.ID, "telefone_cliente_2").click()
            self.driver.find_element(By.ID, "telefone_cliente_2").send_keys("(48)98996-3188")
            self.driver.find_element(By.ID, "email_cliente").click()
            self.driver.find_element(By.ID, "email_cliente").send_keys("emanuel_nunes@inductothermgroup.com.br")
            self.driver.find_element(By.ID, "email_cliente2").click()
            self.driver.find_element(By.ID, "email_cliente2").send_keys("emanuel_nunes@inductothermgroup.com.br")
            self.driver.find_element(By.ID, "senha_cliente").click()
            self.driver.find_element(By.ID, "senha_cliente").send_keys("oJforfAUN5")
            self.driver.find_element(By.ID, "senha_cliente2").click()
            self.driver.find_element(By.ID, "senha_cliente2").send_keys("oJforfAUN5")
            self.driver.find_element(By.CSS_SELECTOR, ".botao-commerce-img").click()
    
   
       
