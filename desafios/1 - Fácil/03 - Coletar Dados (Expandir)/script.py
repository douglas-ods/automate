import sys 
sys.path.append("automate\\config")
from config import Driver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Desafio03:

    def __init__(self) -> None:
        self.navegador = Driver().driver
        self.navegador.get('https://webscraper.io/test-sites/e-commerce/more')
        self.navegador.maximize_window()

    def iniciar(self) -> None:
        def web_scraping(navegador,url):    
            """
            Função que acessa uma url e coleta todos os produtos da página.
            Coleta:
                * Nome
                * Valor
                * Descrição
                * Quantidade de estrelas
                * Quantidade de reviews
            Retorna uma lista de tuplas, onde cada tupla contém os dados coletados.
            """
            navegador.get(url)
            navegador.maximize_window()
            navegador.execute_script("window.scrollTo(0,500)")
            # Aguardar 10 segundos 
            wait = WebDriverWait(navegador, 10)
            while True:
                try:
                    # Aguarde até que o botão esteja presente e clicável
                    botao_expandir = wait.until(EC.element_to_be_clickable(("class name", "ecomerce-items-scroll-more")))                            
                    botao_expandir.click()
                    # Aguarde apenas o tempo necessário para o carregamento dos novos itens
                    wait.until(EC.presence_of_element_located(("class name", "product-wrapper")))        
                except:
                    # Se o botão não estiver mais presente, sai do loop                    
                    break

            # Extrair os dados
            resultados = navegador.find_elements("class name", "product-wrapper")
            lista_produtos = []
            for resultado in resultados:
                nome = resultado.find_element("class name", "title").text
                #print(nome)
                valor = resultado.find_element("class name", "price").text.replace("$", "")
                #print(valor)
                descricao = resultado.find_element("class name", "description").text
                #print(descricao)
                # Classe que contem a quantidade de estrelas
                ratings_element = navegador.find_element("class name", "ratings")
                # Localize o segundo parágrafo dentro do elemento "ratings"
                segundo_paragrafo = ratings_element.find_elements("tag name", "p")[1]
                # Contando a quantidade de elementos <span> existe no segundo parágrafo
                spans_no_segundo_paragrafo = segundo_paragrafo.find_elements("tag name", "span")
                qtd_estrelas = len(spans_no_segundo_paragrafo)
                #print(qtd_estrelas)          
                qtd_reviews = resultado.find_element("class name", "review-count").text.replace("reviews", "")    
                #print(qtd_reviews)
                lista_produtos.append((nome, valor, descricao, qtd_estrelas, qtd_reviews))
            return lista_produtos
        
        url="https://webscraper.io/test-sites/e-commerce/more/computers/laptops"
        lista_laptops = web_scraping(self.navegador,url)
        url = "https://webscraper.io/test-sites/e-commerce/more/computers/tablets"
        lista_tablets = web_scraping(self.navegador,url)
        url = "https://webscraper.io/test-sites/e-commerce/more/phones/touch"
        lista_telefones = web_scraping(self.navegador,url)

        def export_file_excel(lista_dados,dir_output,nome_arquivo):
            """
            Exporta uma lista de produtos para um arquivo excel.
            
            Argumentos:
            lista_dados -- lista de produtos, onde cada produto é uma tupla contendo nome, valor, descri o, quantidade de estrelas e quantidade de reviews
            dir_output -- diretório onde o arquivo excel vai ser salvo
            nome_arquivo -- nome do arquivo excel a ser salvo
            
            As planilhas criadas no arquivo excel ser o:
            - Valor: lista de produtos ordenados por valor (Menor - Maior)
            - Reviews: lista de produtos ordenados por quantidade de reviews (Maior - Menor)
            - Estrelas: lista de produtos ordenados por quantidade de estrelas (Maior - Menor)
            """
            df = pd.DataFrame(lista_dados, columns=["nome", "valor", "descricao", "qtd_estrelas", "qtd_reviews"])
            df["valor"] = df["valor"].astype(float)
            df["qtd_estrelas"] = df["qtd_estrelas"].astype(int)
            df["qtd_reviews"] = df["qtd_reviews"].astype(int)
            
            df_valor = df.sort_values(by="valor", ascending=True)
            df_qtd_reviews = df.sort_values(by="qtd_reviews", ascending=False)
            df_estrelas = df.sort_values(by="qtd_estrelas", ascending=False)

            with pd.ExcelWriter(f'{dir_output}\\{nome_arquivo}.xlsx') as writer:
                df_valor[["nome", "valor"]].to_excel(writer, sheet_name='Valor', index=False)
                df_qtd_reviews[["nome", "qtd_reviews"]].to_excel(writer, sheet_name='Reviews', index=False)
                df_estrelas[["nome", "qtd_estrelas"]].to_excel(writer, sheet_name='Estrelas', index=False)
                
        # Exporta os arquivos        
        export_file_excel(lista_laptops,"automate\desafios\\1 - Fácil\\03 - Coletar Dados (Expandir)","laptops")
        export_file_excel(lista_tablets,"automate\desafios\\1 - Fácil\\03 - Coletar Dados (Expandir)","tablets")
        export_file_excel(lista_telefones,"automate\desafios\\1 - Fácil\\03 - Coletar Dados (Expandir)","telefones")
        
        
        self.navegador.quit()

        input()


if __name__ == '__main__':
    Desafio03().iniciar()
