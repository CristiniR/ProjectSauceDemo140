import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_3_Login_Positivo():

    url = "https://www.giulianaflores.com.br/"                 


    def setup_method(self, method):                  
        self.driver = webdriver.Chrome()              
        self.driver.implicitly_wait(10)               

    def teardown_method(self, method):                
        self.driver.quit()              

    # login ok ---------------------------------------------------------------------------------------------------------------               
   
    def test_selecionar_produto(self):                
        self.driver.get(self.url)
        self.driver.find_element(By.ID,"perfil-hidden").click()
        self.driver.find_element(By.ID,"UrlLogin").click()
        self.driver.find_element(By.ID,"ContentSite_txtEmail").send_keys("663.467.512-04")                     
        self.driver.find_element(By.ID,"ContentSite_txtPassword").send_keys("YZDfCBhl0k")
        self.driver.find_element(By.ID,"ContentSite_ibtContinue").click()
        self.driver.find_element(By.ID,"perfil-hidden").click()
        self.driver.find_element(By.CSS_SELECTOR, "li > a:nth-child(2)").click()
        