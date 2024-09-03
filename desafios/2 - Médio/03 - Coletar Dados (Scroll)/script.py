import sys 
sys.path.append("C:\\automate\\config")
from config import Driver
import pandas as pd
import time


class Desafio03:

    def __init__(self) -> None:
        self.navegador = Driver().driver
        self.navegador.get('https://webscraper.io/test-sites/e-commerce/scroll')
        self.navegador.maximize_window()

    def iniciar(self) -> None:
        # Seu script aqui.
        def web_scraping(navegador,url):            
            """
            Função que acessa uma url e coleta todos os produtos da página, realizando scroll para carregar todos os produtos.
            Argumentos:
            - navegador (selenium.webdriver): Navegador selenium para acesso à página.
            - url (str): URL da página a ser acessada.
            Retorna:
            - lista_produtos (list): Lista de produtos coletados.
            """
            navegador.get(url)
            navegador.maximize_window()    
            # Aguarde o carregamento inicial da página
            navegador.implicitly_wait(5)    
            # Variável para armazenar a quantidade de produtos carregados
            qtd_produtos_anterior = 0    
            while True:
                # Role até o final da página
                navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")        
                # Aguarde um tempo para que os novos produtos carreguem
                time.sleep(3)          
                # Coletar todos os produtos visíveis na página
                produtos = navegador.find_elements("class name", "product-wrapper")        
                # Se o número de produtos for o mesmo após o scroll, a página acabou de carregar
                if len(produtos) == qtd_produtos_anterior:
                    break  # Saia do loop quando não houver novos produtos carregados        
                # Atualize o contador de produtos carregados
                qtd_produtos_anterior = len(produtos)

            # Extração de dados 
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
                # Localiza o segundo parágrafo dentro do elemento "ratings"
                segundo_paragrafo = ratings_element.find_elements("tag name", "p")[1]
                # Contando a quantidade de elementos <span> existe no segundo parágrafo
                spans_no_segundo_paragrafo = segundo_paragrafo.find_elements("tag name", "span")
                qtd_estrelas = len(spans_no_segundo_paragrafo)
                #print(qtd_estrelas)          
                qtd_reviews = resultado.find_element("class name", "review-count").text.replace("reviews", "")    
                #print(qtd_reviews)
                lista_produtos.append((nome, valor, descricao, qtd_estrelas, qtd_reviews))

            return lista_produtos
        
        url = "https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops"
        lista_laptops = web_scraping(self.navegador,url)
        url = "https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets"
        lista_tablets =  web_scraping(self.navegador,url)
        url = "https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
        lista_telefones =  web_scraping(self.navegador,url)

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

        # Exportando os arquivos...            
        export_file_excel(lista_laptops,"C:\\automate\desafios\\2 - Médio\\03 - Coletar Dados (Scroll)","laptops")
        export_file_excel(lista_tablets,"C:\\automate\desafios\\2 - Médio\\03 - Coletar Dados (Scroll)","tablets")
        export_file_excel(lista_telefones,"C:\\automate\desafios\\2 - Médio\\03 - Coletar Dados (Scroll)","telefones")
                
        self.navegador.quit()

        input()


if __name__ == '__main__':
    Desafio03().iniciar()
