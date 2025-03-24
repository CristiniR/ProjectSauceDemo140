Feature: Lista_exercicios_07

    Scenario Outline: Cadastro Usuário 
        Given que acesso o site advantageonlineshopping
        When acesso a pagina de cadastro
        Then preencho os dados de cadastro com Username <Username> Password <Password> Email <Email> Confirmpassword <Confirmpassword> 
        Then aceito os termos de privacidade e clico no botão registrar

        Examples:
            | id | Username  | Password   | Email                    | Confirmpassword |
            | 01 | MariaM    | lZSQ7Szxq0 | maria.maria@dkcarmo.com  | lZSQ7Szxq0      | 
            
    Scenario: Compra a partir de um banner na home 
        Given que acesso o site advantageonlineshopping
        When acesso a pagina de login 
        Then preencho os campos de login com Username MariaM e Password lZSQ7Szxq0
        When estou na pagina home clico no banner de Tablets 
        Then valido se estou na página de Tablets
        When seleciono o produto "HP ELITEPAD 1000 G2 TABLET" 
        Then valido o nome do produto e o valor
        When adiciono o produto "HP ELITEPAD 1000 G2 TABLET" ao carrinho de compras
        Then valido se estou no carrinho de compras e a quantidade adicionada
        Then removo o produto "HP ELITEPAD 1000 G2 TABLET" do carrinho de compras
        Then acesso o menu faço o logout

    Scenario Outline: Login com credenciais inválidas
        Given que acesso o site advantageonlineshopping
        When acesso a pagina de login 
        Then preencho os campos de login com Username <Username> e Password <Password>
        Then exibe a <mensagem> de erro quando o login não é o correto

        Examples:
            | id | Username        | Password       | mensagem                           |
            | 01 | MariaM          | SenhaErrada    | Incorrect user name or password.   |
            | 02 | LoginErrado     | lZSQ7Szxq0     | Incorrect user name or password.   |
            | 03 | LoginErrado     | SenhaErrada    | Incorrect user name or password.   |


