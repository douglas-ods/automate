# automate

Teste suas habilidades de automação com essa playlist de desafios variados.
___

## Configurando o Ambiente

1. Instalar o [Python](https://www.python.org/) na versão `3.12`
2. Instalar o [Git](https://git-scm.com/)
3. Realizar
   um [fork](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
   do repositório [automate](https://github.com/jaymeklein/automate)
4. Realizar um [git clone](https://git-scm.com/docs/git-clone) do seu repositório resultante do `fork`
5. Acessar a pasta `automate`, raiz do repositório.
6. Criar o [venv](https://docs.python.org/3/library/venv.html) do python
   ```bash
   python -m venv venv 
   ```
7. Ativar o `venv` criado:
   ```bash
   .\venv\Scripts\activate
   ```
   ou
   ```bash
   venv\Scripts\activate.bat
   ```
   OBS: Dependendo da IDE usada, será necessário configurar o venv manualmente.
   Há diversos tutoriais no youtube para estas configurações:
    * [VSCode](https://www.youtube.com/watch?v=O0bYaxUINnE)
    * [PyCharm](https://www.youtube.com/watch?v=2P30W3TN4nI)

8. Instalar as bibliotecas:
   ```bash
   pip install -r requirements.txt
   ```

9. Se nenhum erro ocorreu até o momento, os desafios estão prontos para serem feitos.

___

## Realizando os Desafios

Dentro da pasta `desafios`, eles estão divididos em fáceis, médios e difíceis. <br>
Cada desafio possui uma série de instruções e um arquivo `script.py` que deverá ser modificado de acordo com o desafio.

1. Fáceis
    * 01 - Coletar dados de uma página web;
    * 02 - Coletar dados de uma página web com paginação;
    * 03 - Coletar dados de uma página web com um botão para carregar mais dados;

2. Médios - Diferencial
    * 01 - Desafio que envolve preencher inputs dinâmicos que trocam de posição na tela;
    * 02 - Agrupar dados de 3 arquivos `.csv` e organizar pastas com base nos dados;
    * 03 - Coletar dados de uma página web em que os dados aparecem conforme o usuário desce a página;

3. Difíceis - Diferencial
    * 01 - Desafio que envolve resolver captchas dinâmicos de texto;


* Evite realizar processos manuais, tente sempre usar o python para manipular os dados.
* Não coloque caminhos "brutos" como  `C:\Users\Fulano\Documents\arquivo.py`
* Alguns desafios podem ter gargalo de desempenho, como o `desafios/2 - Médio/02 - Agrupar Dados (Excel)` e
  o `desafios/3 - Difícil/01 - Text Captcha`, portanto, tente otimizá-los o máximo possível, usando funções `built-in`
  quando possível.

___

## Enviando os Desafios

1. Realize um [git add](https://git-scm.com/docs/git-add) dos arquivos modificados.
2. Realize um [git commit](https://git-scm.com/docs/git-commit) com os arquivos do `add`.
3. Realize um [git push](https://git-scm.com/docs/git-push) do(s) commits realizados.
4. Comunique a equipe Wind da finalização das atividades e nos forneça o link do seu repositório.
5. Libere acesso ao repositório criado para o usuário `jaymeklein`

**OBS: O repositório deverá ser PRIVADO**
___

## Dúvidas

Dúvidas gerais sobre a execução dos desafios poderão ser enviados entrando em contato com a equipe, ou
na [Issue](https://github.com/jaymeklein/automate/issues/1) disponibilizada para este fim.
