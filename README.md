# S16A4-Planilha-de-Vendas

## Desafio
Construir um aplicativo simples que leia os dados, processe e exiba resultados organizados. O programa deve ser em Python e precisa:
* declarar uma matriz 2D representando vendas;
* calcular totais por vendedor;
* calcular totais por mês;
* calcular o total geral;
* identificar o melhor vendedor.

## Etapa 1 – Exibição organizada
Percorra a matriz e exiba os valores organizados por vendedor.
Analise e responda: 
* Quantas linhas existem?
  * R.: 3
* Quantas colunas existem?
  * R.: 3

## Etapa 2 – Total por vendedor
Calcule o total vendido por cada vendedor.

* total vendedor 0; 450
* total vendedor 1; 750
* total vendedor 2: 500

## Etapa 3 – Total por mês
   
 * total mês 0; 500
 * total mês 1; 600
 * total mês 2: 600

## Etapa 4 – Total geral
 * Total geral:
 * R:1700

## Etapa 5 – Melhor vendedor
 * Vendedor 1


## Etapa 6 – Texto explicativo
* Analise todos os passos realizados e responda:
 * Como os laços aninhados foram utilizados?
  * R.: Foram utilizados dois laços for. O primeiro percorre as linhas da matriz, representando os vendedores, e o segundo percorre as colunas, representando os meses. Para calcular os totais por mês, a lógica foi invertida: o primeiro laço percorre as colunas e o segundo percorre as linhas.
    
 * Como foi feito o controle de índices?
  * R.: O índice i foi utilizado para controlar as linhas e o índice j para controlar as colunas. len(vendas) informa a quantidade de linhas, enquanto len(vendas[0]) informa a quantidade de colunas.
    
 * Qual foi o resultado da análise?
  * R.: A empresa realizou 1.700 vendas no total. O vendedor 1 foi o melhor vendedor, com 750 vendas. O mês 0 teve 500 vendas, o mês 1 teve 600 vendas e o mês 2 também teve 600 vendas.
