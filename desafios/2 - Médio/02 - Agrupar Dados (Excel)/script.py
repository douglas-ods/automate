import os
import pandas as pd
import requests
import zipfile
import io

class Desafio02:    
    def iniciar(self) -> None:

        # URL do arquivo .zip
        url = "https://dados.tce.rs.gov.br/dados/licitacon/licitacao/ano/2024.csv.zip"
        # Fazer o download do arquivo .zip
        response = requests.get(url)
        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Abrir o conteúdo do arquivo ZIP em memória
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                # Extrair todo o conteúdo do ZIP para o diretório atual
                diretorio =  'automate\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)'
                zip_ref.extractall(diretorio)
            print("Arquivo baixado e extraído com sucesso!")
        else:
            print(f"Falha no download. Status code: {response.status_code}")

        def deletar_arquivos(lista_arquivos):   
            for caminho_arquivo in lista_arquivos:
                if os.path.exists(caminho_arquivo):
                    os.remove(caminho_arquivo)
                    print(f"Arquivo {caminho_arquivo} deletado com sucesso.")
                else:
                    print(f"Arquivo {caminho_arquivo} não encontrado.")

        lista_arquivos = [
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\proposta.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\pessoas.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\\membrocons.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\lote_prop.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\dotacao_lic.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\licitante.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\comissao.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\memcomissao.csv',    
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\item_prop.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\evento_lic.csv',
            'automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\documento_lic.csv'
            # Adicione mais caminhos completos aqui
        ]
        deletar_arquivos(lista_arquivos)

        # Carregar os DataFrames
        df_licitacao = pd.read_csv("automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\licitacao.csv")
        df_lote = pd.read_csv("automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\lote.csv")
        df_item = pd.read_csv("automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\item.csv")

        # Merge dos DataFrames
        df_join = pd.merge(df_licitacao, df_lote, on=['CD_ORGAO', 'NR_LICITACAO', 'ANO_LICITACAO', 'CD_TIPO_MODALIDADE'])
        df_join = pd.merge(df_join, df_item, on=['CD_ORGAO', 'NR_LICITACAO', 'ANO_LICITACAO', 'CD_TIPO_MODALIDADE', 'NR_LOTE'])


        # Diretório para salvar os arquivos
        output_dir = "automate\\desafios\\2 - Médio\\02 - Agrupar Dados (Excel)\\licitacoes"        
        os.makedirs(output_dir, exist_ok=True)

        # Cria um arquivo `link.txt`, contendo o link presente no `DataFrame` de licitações
        df_join["LINK_LICITACON_CIDADAO"].to_csv(f"{output_dir}\\link.txt",index=False,header=0)

        
        def criar_pastas_arquivos(x):
            # Criar pasta da licitação
            licitacao_folder = os.path.join(
                output_dir,
                f"{x['CD_ORGAO']}_{x['NR_LICITACAO']}_{x['ANO_LICITACAO']}_{x['CD_TIPO_MODALIDADE']}"
            )
            os.makedirs(licitacao_folder, exist_ok=True)
            
            # Criar a pasta `lotes`
            lotes_folder = os.path.join(licitacao_folder, "lotes")
            os.makedirs(lotes_folder, exist_ok=True)
            
            # Criar o arquivo `{NR_LOTE}.csv` para cada lote e salvar os itens correspondentes
            lote_file_path = os.path.join(lotes_folder, f"{x['NR_LOTE']}.csv")
            
            # Selecionar apenas as colunas de interesse para o CSV
            x[['CD_ORGAO', 'NR_LICITACAO', 'ANO_LICITACAO', 'CD_TIPO_MODALIDADE', 'NR_LOTE','DS_ITEM']].to_csv(
                lote_file_path,
                index=False
            )

        # Aplicar a função lambda a cada linha do DataFrame 
        df_join.apply(lambda x: criar_pastas_arquivos(x), axis=1)

        input()


if __name__ == '__main__':
    Desafio02().iniciar()
