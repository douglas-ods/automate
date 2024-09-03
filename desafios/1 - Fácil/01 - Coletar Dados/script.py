import sys 
sys.path.append("automate\\config")
from config import Driver
import pandas as pd

class Desafio01:

    def __init__(self) -> None:
        self.navegador = Driver().driver
        self.navegador.get('https://webscraper.io/test-sites/e-commerce/allinone')
        self.navegador.maximize_window()

    def iniciar(self) -> None:
        # Seu script aqui.        
        def web_scpraing(navegador,url): 
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
            # Extração de dados
            resultados = navegador.find_elements("class name","product-wrapper")
            lista_produtos = []
            for resultado in resultados:
                nome = resultado.find_element("class name","title").text
                #print(nome)
                valor = resultado.find_element("class name","price").text
                valor = valor.replace("$","")
                #print(valor)
                descricao = resultado.find_element("class name","description").text
                #print(descricao)        
                #Localiza o elemento <p> e obtenha o valor do atributo 'data-rating'
                elemento_estrelas = resultado.find_element("css selector", 'p[data-rating]')
                qtd_estrelas = elemento_estrelas.get_attribute('data-rating')
                #print(qtd_estrelas)    
                qtd_reviews = resultado.find_element("class name","review-count").text
                qtd_reviews = qtd_reviews.replace("reviews","")
                #print(qtd_reviews)                
                lista_produtos.append((nome,valor,descricao,qtd_estrelas,qtd_reviews))
                
            return lista_produtos
        
        lista_laptops = web_scpraing(self.navegador,"https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
        lista_tablets = web_scpraing(self.navegador,"https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets") 
        lista_telefones = web_scpraing(self.navegador,"https://webscraper.io/test-sites/e-commerce/allinone/phones/touch")
        
        def export_file_excel(lista_dados,dir_output,nome_arquivo):
            """
            Exporta uma lista de produtos para um arquivo excel.
            
            Argumentos:
            lista_dados -- lista de produtos, onde cada produto é uma tupla contendo nome, valor, descri o, quantidade de estrelas e quantidade de reviews
            dir_output -- diretório onde o arquivo excel vai ser salvo
            nome_arquivo -- nome do arquivo excel a ser salvo            
            
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
        export_file_excel(lista_laptops,"automate\\desafios\\1 - Fácil\\01 - Coletar Dados","laptops")
        export_file_excel(lista_tablets,"automate\\desafios\\1 - Fácil\\01 - Coletar Dados","tablets")
        export_file_excel(lista_telefones,"automate\\desafios\\1 - Fácil\\01 - Coletar Dados","telefones")        
            
        self.navegador.quit()

        input()

if __name__ == '__main__':
    Desafio01().iniciar()
