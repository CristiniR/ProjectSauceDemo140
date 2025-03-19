import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_5_Fluxo_de_compra():

    url = "https://www.giulianaflores.com.br/"                 


    def setup_method(self, method):                  
        self.driver = webdriver.Chrome()              
        self.driver.implicitly_wait(13)               

    def teardown_method(self, method):                
        self.driver.quit()              

    # Compra a partir de um banner---------------------------------------------------------------------------------------------------
        
    def test_selecionar_produto(self):                
        self.driver.get(self.url)
        self.driver.get(self.url)
        self.driver.find_element(By.ID,"perfil-hidden").click()
        self.driver.find_element(By.ID,"UrlLogin").click()
        self.driver.find_element(By.ID,"ContentSite_txtEmail").send_keys("663.467.512-04")                     
        self.driver.find_element(By.ID,"ContentSite_txtPassword").send_keys("YZDfCBhl0k")
        self.driver.find_element(By.ID,"ContentSite_ibtContinue").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".txtDeliveryAddress > span").click()
        self.driver.find_element(By.CSS_SELECTOR,".apply-button").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .title-item").text == "Aromatizador Home Spray Linha Encontro Floral Giuliana Flores"
        assert self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .actual-price").text == "R$ 89,90"
        self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .product-item img").click()
        assert self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "AROMATIZADOR HOME SPRAY LINHA ENCONTRO FLORAL GIULIANA FLORES"
        assert self.driver.find_element(By.CSS_SELECTOR, ".preco_prod > .precoPor_prod").text == "R$ 89,90"
        self.driver.find_element(By.ID,"ContentSite_lbtBuy").click()
        self.driver.find_element(By.ID,"btConfirmShippingData").click()
        