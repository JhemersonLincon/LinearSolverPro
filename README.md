<h1 align="center"> LinearSolver Pro - Software para resolução de problemas de otimização Linear</h1>

## Descrição do Projeto
<p align="justify">Este software está sendo desenvolvido como parte de um projeto acadêmico no curso de Sistemas de Informação, na disciplina de Pesquisa Operacional. Nosso objetivo é aplicar os conceitos teóricos aprendidos em sala de aula para desenvolver uma solução prática e eficiente para resolver problemas complexos de otimização.</p>


<img src="https://img.shields.io/static/v1?label=Python&message=language&color=blue&style=for-the-badge&logo=Python"/>

<img src="https://img.shields.io/static/v1?label=Html&message=HTML\CSS&color=red&style=for-the-badge&logo=css3"/>
<img src="https://img.shields.io/static/v1?label=Javascript&message=language&color=yellow&style=for-the-badge&logo=javascript"/>


## Requisitos
- [ ] Front-End - Interface para interação do usuário - Em desenvolvimento
- [ ] Back-End - Aplicação dos Métodos - Em desenvolvimento 
- [ ] Back-End - Conexão do Front com o Back - Em desenvolvimento 
- [ ] Documentação - Em desenvolvimento


> Status do Projeto: Em desenvolvimento :warning:

## Desenvolvimento do Software
O Desenvolvimento do software ficou dividida entre quatro pessoas, mas no intuito que cada um pudesse comentar e ajudar durante a criação do software.
<p>Abaixo, fornecemos mais informações sobre cada parte do projeto e seu respectivo andamento:</p>

### Front-end

<div display="flex">
<img src="https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javaScript&logoColor=White&style=fot-the-badge"/>
<img src="https://img.shields.io/badge/-Html-E34F26?logo=html5&logoColor=white&style=fot-the-badge"/>
<img src="https://img.shields.io/badge/-Css3-1572B6?logo=css3&logoColor=white&style=fot-the-badge"/>
</div>

***Responsáveis:***
- Charles Nunes
- João Pedro

#### 📌Interfaces - Charles Nunes
- Foi utilizada a linguagem <b>JavaScript</b> para gerar a tabela de restrições com base nos dados do formulário.

| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `Número de restrições` | `Inteiro` | Define a quantidade de linhas da tabela |
| `Número de variáveis` | `Inteiro` | Define a quantidade de colunas da tabela |

- Ao clicar no botão `Criar tabela` será criada uma tabela onde cada célula receberá valores referentes a cada variável em sua respectiva restrição.
- Após preencher todos os campos e clicar no botão `Enviar Dados` todas as informações serão enviadas para o backend via API.
- No momento a integração com a API não está implementada, porém, é possível visualizar os dados enviados no `console` do navegador. 
***As interfaces poderão sofrer alterações em sua estrutura***

#### 📌Plotagem dos Graficos - João Pedro

Foi encontrado em um framework chamado <b>Flot</b> a base para o desenvolvimento da parte de gráficos do sistema.

### Back-end 
<div display="flex">
<img src="https://img.shields.io/badge/-Python-02569B?logo=Python&logoColor=white&style=fot-the-badge"/>
<img src="https://img.shields.io/badge/-Flask-000000?logo=Flask&logoColor=white&style=fot-the-badge"/>
<img src="https://img.shields.io/badge/-Insomnia-4000BF?logo=Insomnia&logoColor=white&style=fot-the-badge"/>
</div>


***Responsáveis:***
- Jhemerson Lincon Pereira da Silva
- Talita Santos Cordeiro

#### 📌Aplicação do Front e conexão com o Back-end - Talita Santos

- Foi utilizada a biblioteca <b>Flask</b> para criar uma <b>API</b> que permite a interação entre o Front-end e o Back-end, realizando solicitações <b>POST</b>.
  ```http
  POST /methodSimplex
  
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Valor de Z` | `Lista` | Contém a linha do resultado de Z|
| `Matriz final` | `Matriz` | Contém a Matriz da última interação|
| `Matriz de interação` | `Matriz` | Contém um matriz contendo cada interação|

***Sujeito a alteração***

#### 📌Aplicação dos Métodos - Jhemerson Lincon

***Os dados necessários para aplicação dos algoritmos são:***

| Parâmetro   | Tipo       | Descrição                           | Exemplo |
| :---------- | :--------- | :---------------------------------- | :-------|
| `Função` | `Lista` | Contem a função Z| [3,5] |
|  `Minimizar ou Maximizar` | `String`| Se o objetivo é maximizar ou minimizar a função
| `Matriz do lado esquerdo` | `Matriz` | Contém a Matriz do lado esquerdo do problema | [[2,1],[1,2]] |
| `Restrição maior menor` |`Matriz` | Contém uma matriz de string contendo <= ou >= | ["<=","<="] |
| `Matriz do lado direito` | `Matriz` | Contém um matriz contendo cada interação| [4,3] |

***Métodos já aplicados***
- Método Simplex
- Método Dual Simplex


## Documentação
***Responsáveis:***
- João Pedro
- Talita Santos
