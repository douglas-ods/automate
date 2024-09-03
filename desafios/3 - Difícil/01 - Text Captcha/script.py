import sys 
sys.path.append("automate\\config")
from config import Driver
import time 
import re
from PIL import Image 

class Desafio01:
    def __init__(self) -> None:
        self.navegador = Driver().driver
        #self.navegador.get('https://rpachallenge.com/')
        self.navegador.maximize_window() 
    def iniciar(self) -> None: 
        # Seu script aqui.            

        def remover_caracteres_especiais(texto):
            # Expressão regular para substituir qualquer caractere que não seja letra, número ou espaço por uma string vazia
            texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
            return texto_limpo

        try:
            url = "https://captcha.com/demos/features/captcha-demo.aspx"
            # Acesse a página desejada
            self.navegador.get(url)
            self.navegador.maximize_window()    
            # Aguarde 3 segundos
            time.sleep(3)    
            # Localiza o elemento desejado
            captcha_image = self.navegador.find_element("id", "demoCaptcha_CaptchaImage")    
            # Capture um screenshot da tela inteira
            self.navegador.save_screenshot("automate\desafios\\3 - Difícil\\01 - Text Captcha\\img\\tela_inteira.png")    
            # Obtenha a posição e dimensões do elemento
            location = captcha_image.location
            size = captcha_image.size    
            # Calcule as coordenadas do retângulo de corte
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']    
            # Abre a imagem completa
            imagem_completa = Image.open("automate\desafios\\3 - Difícil\\01 - Text Captcha\\img\\tela_inteira.png")    
            # Corta a imagem para pegar somente o elemento desejado
            img_captcha = imagem_completa.crop((left, top, right, bottom))    
            # Salve o screenshot do elemento
            img_captcha.save("automate\desafios\\3 - Difícil\\01 - Text Captcha\\img\\captcha.png")  

            
            try:
                # Abre uma nova aba para acessar o Google Lens
                self.navegador.execute_script("window.open('');")  
                # Muda para a nova aba
                self.navegador.switch_to.window(self.navegador.window_handles[1]) 
                # Acessa o Google Imagens
                self.navegador.get("https://lens.google.com")
                self.navegador.maximize_window()
                # Aguarde o carregamento do Google Lens
                time.sleep(4)  
                # Upload da imagem
                upload_button = self.navegador.find_element("css selector", "input[type='file']")
                upload_button.send_keys("automate\desafios\\3 - Difícil\\01 - Text Captcha\\img\\captcha.png")
                time.sleep(6)
                # Clica no Texto
                texto = self.navegador.find_element("id","text")
                texto.click()
                time.sleep(4)
                # Clica em selecionar todo texto
                selecionar_texto = self.navegador.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/button/span')
                if selecionar_texto.is_displayed():
                    #print("ok")
                    selecionar_texto.click()
                else:
                    print("erro")
                time.sleep(2)
                # Extrai o texto
                text_image = self.navegador.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/span/div/h1').text
                print(text_image)
                texto_processado = remover_caracteres_especiais(text_image)
                print(texto_processado)
            except:
                print("Não foi possível extrair o texto da imagem")
                self.navegador.quit()
                
            
            # Volta para a primeira aba
            self.navegador.switch_to.window(self.navegador.window_handles[0])  
            codigo_captcha = self.navegador.find_element("id","captchaCode")
            codigo_captcha.click()
            codigo_captcha.send_keys(texto_processado)
            validate = self.navegador.find_element("id","validateCaptchaButton")
            validate.click()  
            time.sleep(3)
            try:
                label_correto = self.navegador.find_element("class name","correct")
                if label_correto.is_displayed():
                    print("Passou pelo Captcha")  
            except:
                print("Erro na extração dos caracteres!")
            
        finally:
            # Aguarda 5 segundos
            time.sleep(5)  
            # Fecha o navegador após a conclusão
            self.navegador.quit()

        input()


if __name__ == '__main__':
    Desafio01().iniciar()
