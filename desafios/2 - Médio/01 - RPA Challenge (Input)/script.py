import sys 
sys.path.append("automate\\config")
from config import Driver
import pandas as pd

class Desafio01:

    def __init__(self) -> None:
        self.navegador = Driver().driver
        self.navegador.get('https://rpachallenge.com/')
        self.navegador.maximize_window()

    def iniciar(self) -> None:
        # Seu script aqui.
        df = pd.read_excel("automate\\desafios\\2 - Médio\\01 - RPA Challenge (Input)\\challenge.xlsx")        
        #self.navegador.get("https://rpachallenge.com/")
        self.navegador.maximize_window()
        self.navegador.execute_script("window.scroll(0,1000)")
        start = self.navegador.find_element("class name","btn-large")
        start.click()
        for i in df.index:
            first_name =      df.loc[i,"First Name"]
            last_name =       df.loc[i,"Last Name "]
            company_name =    df.loc[i,"Company Name"]
            role_in_company = df.loc[i,"Role in Company"]
            address =         df.loc[i,"Address"]
            email =           df.loc[i,"Email"]
            phone_number =    df.loc[i,"Phone Number"]
            primeiro_nome = self.navegador.find_element("css selector","input[ng-reflect-name='labelFirstName']")
            primeiro_nome.click()     
            primeiro_nome.send_keys(str(first_name))               
            ultimo_nome= self.navegador.find_element("css selector","input[ng-reflect-name='labelLastName']")
            ultimo_nome.click()
            ultimo_nome.send_keys(str(last_name))                
            nome_empresa= self.navegador.find_element("css selector","input[ng-reflect-name='labelCompanyName']")
            nome_empresa.click()
            nome_empresa.send_keys(str(company_name))             
            funcao_empresa=  self.navegador.find_element("css selector","input[ng-reflect-name='labelRole']")
            funcao_empresa.click()
            funcao_empresa.send_keys(str(role_in_company))            
            endereco= self.navegador.find_element("css selector","input[ng-reflect-name='labelAddress']")
            endereco.click()
            endereco.send_keys(str(address))               
            mail= self.navegador.find_element("css selector","input[ng-reflect-name='labelEmail']")
            mail.click()
            mail.send_keys(str(email))                 
            numero_telefone = self.navegador.find_element("css selector","input[ng-reflect-name='labelPhone']")
            numero_telefone.click()
            numero_telefone.send_keys(str(phone_number))            
            submit = self.navegador.find_element("xpath","/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
            submit.click()
        
        self.navegador.quit()
        
        input()


if __name__ == '__main__':
    Desafio01().iniciar()
