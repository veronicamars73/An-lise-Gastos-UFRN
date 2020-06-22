# Introdução

Análise de gastos por unidade da Universidade Federal do Rio Grande do Norte.

## Base de Dados

A base de dados escolhida foi a Relação de gastos por unidades da UFRN disponível no site dados.gov.br, foi usado o documento csv disponibilizado no endereço: [link para base](http://www.dados.gov.br/dataset/gastos). Tal arquivo contém os seguintes campos:
![Quadro 1: Campos da base de dados - Fonte: Dados Abertos | UFRN](images/campos_bd.png)

## Introdução à Base de Dados

A base de dados representa os gastos por unidade da UFRN desde o ano de 2000 até o ano de 2020. 
As variáveis da base são: **id_unidade**, que corresponde ao número identificador da unidade e que é uma variável qualitativa nominal; **unidade**, que corresponde ao nome da unidade que realizou o gasto e pode ser classificada como uma variável qualitativa nominal; **natureza_despesa**, que classifica a motivação do gasto e é uma variável qualitativa nominal; **Ano**, que marca qual o ano da movimentação financeira e pode ser classificada como quantitativa discreta e **valor** que apresenta o valor exato do gasto da movimentação.
As unidades amostrais da base são as unidades da universidade, porém para facilitação de observação dos dados e considerando o provável elevado tamanho da base de dados analisaremos somente os dados do Instituto Metrópole Digital. Como o IMD só foi fundado em 2011 esperamos que só tenhamos dados a partir dessa data. Ademais, esperamos que no ano de 2020 os dados apresentem uma considerável diminuição em consequência da pandemia que ocasionou uma suspensão nas atividades do instituto.

## Análise dos Dados

Com o auxílio da linguagem de programação *python* e as bibliotecas *pandas*, *seaborn* e *matplotlib* foi desenvolvido gráficos com informações sobre os gastos do Instituto Metrópole Digital e tabelas (via *pandas*) com dados do instituto e dados gerais.
O arquivo `saida.xlsx` contém os dados completos fornecidos pelo csv, como esperado, é uma planilha bastante extensa.
Após a separação dos dados do Instituto Metrópole Digital dos dados fornecidos foi realizada a criação de uma tabela com todas as ações financeiras do IMD na base que corresponde ao arquivo `saida_only_imd.xlsx` e uma tabela com o somatório anual de ações do instituto que corresponde ao `year_sum.xlsx`.
Além disso com a *Seaborn* e a *Matplotlib* foi criado um gráfico com os valores gastos anualmente pela unidade de 2011 a 2020. O gráfico pode ser melhor visualizado ao executar o arquivo `main.py` e pode ser visualizado no arquivo `graph_imd_gastos.png` (sem completa resolução).
