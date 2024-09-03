import sys 
sys.path.append("automate\\config")
from config import Driver
import pandas as pd

class Desafio02:

    def __init__(self) -> None:
        self.navegador = Driver().driver
        self.navegador.get('https://webscraper.io/test-sites/e-commerce/static')
        self.navegador.maximize_window()

    def iniciar(self) -> None:
        def web_scraping(navegador,url_inicial,url_final):            
            """
            Função para coletar dados de uma página com paginação.
            Argumentos:
            - navegador (selenium.webdriver): Navegador selenium para acesso à página.
            - url_inicial (str): URL da página inicial.
            - url_final (str): URL da página final, que deve conter o número da página na URL.
            Retorna:
            - lista_produtos (list): Lista de produtos coletados.
            """
            navegador.get(url_inicial)    
            navegador.maximize_window()    
            # Localiza o elemento que contém o número da última página
            ultima_pagina_elemento = navegador.find_elements("css selector", 'ul.pagination li.page-item a.page-link')[-2]
            ultima_pagina = int(ultima_pagina_elemento.text)
            #print(f"Número da última página: {ultima_pagina}")    
            # Iterar sobre todas as páginas
            lista_produtos = []
            for pagina in range(1, ultima_pagina + 1):
                #print(f"Acessando a página: {pagina}")
                navegador.get(f"{url_final}{pagina}")        
                navegador.implicitly_wait(5)        
                # Extração de dados
                resultados = navegador.find_elements("class name", "product-wrapper")        
                for resultado in resultados:
                    nome = resultado.find_element("class name", "title").text
                    valor = resultado.find_element("class name", "price").text.replace("$", "")
                    descricao = resultado.find_element("class name", "description").text
                    elemento_estrelas = resultado.find_element("css selector", 'p[data-rating]')
                    qtd_estrelas = elemento_estrelas.get_attribute('data-rating')
                    qtd_reviews = resultado.find_element("class name", "review-count").text.replace("reviews", "")
                    lista_produtos.append((nome, valor, descricao, qtd_estrelas, qtd_reviews))

            return lista_produtos
        
        pagina_inicial_laptops = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1"
        pagina_final_laptops = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
        lista_laptops = web_scraping(self.navegador,pagina_inicial_laptops,pagina_final_laptops)
        pagina_inicial_tablets = "https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page=1"
        pagina_final_tablets = "https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page="
        lista_tablets = web_scraping(self.navegador,pagina_inicial_tablets,pagina_final_tablets)
        pagina_inicial_tel = "https://webscraper.io/test-sites/e-commerce/static/phones/touch?page=1"
        pagina_final_tel = "https://webscraper.io/test-sites/e-commerce/static/phones/touch?page="
        lista_telefones = web_scraping(self.navegador,pagina_inicial_tel,pagina_final_tel)

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
        export_file_excel(lista_laptops,"automate\desafios\\1 - Fácil\\02 - Coletar Dados (Paginação)","laptops")
        export_file_excel(lista_tablets,"automate\desafios\\1 - Fácil\\02 - Coletar Dados (Paginação)","tablets")
        export_file_excel(lista_telefones,"automate\desafios\\1 - Fácil\\02 - Coletar Dados (Paginação)","telefones")

        
        self.navegador.quit()
            
        input()


if __name__ == '__main__':
    Desafio02().iniciar()
