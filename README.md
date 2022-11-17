## Sobre

A ideia desse projeto é criar um modelo de Machine Learning capaz de fazer a análise de crédito de uma pessoa. O modelo será treinado com dados de pessoas que já possuem um histórico de crédito e com isso será possível prever se uma pessoa será ou não aprovada para um crédito.

<img src="https://i.ibb.co/sbgNLjf/cedit-risk.png" alt="Análise de Risco"/>

## Como usar

### Configurando o banco de dados

Para importar os dados, basta executar o script `/src/assets/data.sql` no seu banco de dados MySQL.

Após importar os dados, é ncessário configurar as credenciais de acesso ao banco de dados no arquivo `src/contants.py`, na classe **DatabaseConfig**.

### Instalando as bibliotecas necessárias

[]: # Language: python
[]: # Path: requirements.txt
[]: # Name: requirements.txt
[]: # Type: file
[]: # Description: Arquivo de dependências do projeto
[]: # Tags: python, requirements, dependências

```bash
pip install -r requirements.txt
```

### Criando o modelo de Machine Learning

Execute todos os passos dentro do arquivo `src/credit-analysis-model.ipynb`, para criar o modelo de Machine Learning para análise de crédito.

1. Esse arquivo poderá ser aberto no Jupyter Notebook ou no Google Colab.
2. **(Recomendado)** Se quiser acessar pelo Visual Studio Code, instale as extensões [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) e [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) e abra o arquivo `src/credit-analysis-model.ipynb`.
3. Caso tenha o PyCharm na versão Professional, recomendo a utilização do mesmo por já configurar o JuPyter facilmente.


### Executando a aplicação para análise de crédito

[]: # Language: python
[]: # Path: src/main.py
[]: # Name: main.py
[]: # Type: file
[]: # Description: Arquivo principal do projeto
[]: # Tags: python, main, principal

```bash
streamlit run src/main.py
```

### Executando os testes

[]: # Language: python
[]: # Path: src/tests.py
[]: # Name: tests.py
[]: # Type: file
[]: # Description: Arquivo de testes do projeto
[]: # Tags: python, tests, testes

```bash
pytest src/tests.py
```

## 👥 Autores
<table  style="text-align:center; border: none" >
<tr>

<td align="center"> 
<a href="https://github.com/itmoura" style="text-align:center;">
<img style="border-radius: 20%;" src="https://github.com/itmoura.png" width="120px;" alt="autor"/><br> <strong> Ítalo Moura </strong>
</a>
</td>

<td align="center"> 
<a href="https://github.com/dimeleone" styles="text-align:center;">
<img style="border-radius: 20%;" src="https://github.com/dimeleone.png" width="120px;" alt="autor"/><br><strong> Dimitri Leone </strong>
</a>
</td>

</tr>
</table>

## Licença

[MIT](https://choosealicense.com/licenses/mit/)


