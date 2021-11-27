# etl_medals

This is a school job for ETL practice for unisinos. Received columns are label as english due to dataset, but output tables will be translated to portuguese (pt-br)

## Business

1. Escolher ou criar uma base de dados (Staging); 
    - [Tokyo Olympics 2021](https://www.kaggle.com/arjunprasadsarkhel/2021-olympics-in-tokyo)
1. Modelar, pelo menos, três tabelas dimensão, sendo uma de cada tipo das atualizações (SCD) vistas em aula. Explicações abaixo são baseadas no site [O que significa e qual a importância do SCD no Data Warehouse](https://canaltech.com.br/infra/O-que-significa-e-qual-a-importancia-do-SCD-no-Data-Warehouse/)
    - SCD 1 `alteração que não armazena histórico na dimensão`:
        - Atletas.csv
        - motivação para essa proposta: os atletas se inscrevem antes nas olimpiadas e salvo excessões, se mantém estáticos. Assumo que a saída de um atleta não possa ser substituída
    - SCD 2: `adicionado um novo registro com as mudanças, preservando sempre os dados anteriores`
        - Medalhas.csv
        - movitação: Preservar todo o histórico de mudanças dos países e seus ranks
    - SCD 3: `Essa técnica funciona com a adição de uma nova coluna na tabela de dimensão, onde é armazenada a atualização, mantendo na antiga coluna o valor anterior`
        - Coaches.csv
        - movitação: será armazenado somente o ultimo e penultimo técnico atrelado a um time imaginando que possam ocorrer trocas ao longo das olimpiadas mas que não sejam constantes.
1. Modelar pelo menos uma tabela fato; 
    - Tabelas fatos: Atletas, Medalhas e Treinadores
1. Popular com dados as tabelas dimensão e a(s) tabela(s) fato(s); 
    - Dimensão: Jogos, Eventos, Paises
    - inicialmente foi utilizado Talend com input excel e output de para uma base de dados SQLite, porém como o job não conectava ao banco, foi trocado a prática.
1. Criar uma visualização de dados utilizando as tabelas construídas.  
    - Será montado em um excel

## Python

1. Use pip3
1. Install openpyxl, pandas with pip3
### How to run

Run `main.py`

## Datasets

- [Tokyo Olympics 2021](https://www.kaggle.com/arjunprasadsarkhel/2021-olympics-in-tokyo)

## Tokyo Olympics Received Dataset

Table **Athlets**
|Column|Attribute Type| 
|---------|---------|
|Name|String|
|Country (original column is NOC)|String|
|Game (original column is Discipline)|String|

Table **Coach**
| Column | Attribute Type| 
|---------|---------|
|Name|String|
|Country (original column is NOC)|String|
|Game (original column is Discipline)|String|
|Event|String|

Table **Entry Gender**
| Column | Attribute Type| 
|---------|---------|
|Name|String|
|Male|Integer|
|Female|Integer|
|Total|Integer|

Table **Medals**
| Column | Attribute Type| 
|---------|---------|
|Rank|Integer|
|Team/NOC|String|
|Gold|Integer|
|Silver|Integer|
|Bronze|Integer|
|Total|Integer|
|Rank by Total|Integer|

Table **Teams**
| Column | Attribute Type| 
|---------|---------|
|Name|String|
|NOC|String|
|Event|String|
|Discipline|String|

## Dataset Analysis

Below there is a list of points that were raised by me while looking the table structure. They are classified as 1) [IMPROVEMENT] where I see I can remove duplications or improve structure 2) [INCONSISTENCIES] due to the data structure I'm not be able to deep the relation between tables due to missing information 

1. [IMPROVEMENT] There are duplications in these tables, where NOC, Event and Discipline appear in different tables as their string values, instead of a simple reference ID.
2. [IMPROVEMENT] Tables don't have an ID property to act as a PK. This could be added.
3. [IMPROVEMENT] There is no direct relation between Coaches and Athletes. I can still create a relation based on Country and Games. If I create tables to Countries and Games this would become easier
4. [INCONSISTENCIES] Athletes table don't have gender information. Entry Gender table may not be used due to this.
5. [IMPROVEMENT/INCONSISTENCIES] Ideally I would create a table Games where I would have the information realted to NOC and Event, but since the Athletes table doesn't have the event information, I don't think I would be able to unless I had a relation 1 Athlete to N games. But I don't know if this makes sense. @TODO need to search olympics rules to do this.
6. [INCONSISTENCIES] Events from Teams and Coaches do not match!

## Tokyo Olympics Proposed Dataset

This is how I think these tables would look like with my suggested improvements

PK - primary key
RK - reference key

Table **Atletas**
|Column|Attribute Type|Column Type| 
|---------|---------|---------|
|ID|Intenger|PK|
|Nome|String||
|Pais|Intenger| RK to Paises|
|Jogo|Integer|RK to Jogos|
|Time|Integer|RK to Times|

Assuming relation 1 Athlete:1 Game as of now

Table **Treinadores**
| Column | Attribute Type| Column Type| 
|---------|---------|---------|
|ID|Intenger|PK|
|Nome|String||
|Pais|Intenger| RK to Paises|
|Jogo|Integer|PK to Jogos|
|Eventos|Intenger|PK to Eventos|

Assuming relation 1 Coach:1 Game as of now
Assuming relation 1 Coach:1 Event as of now

Table **Entry Gender**

This table will be ignored due to [Dataset Analysis](#dataset-analysis)

Table **Medalhas**
| Column | Attribute Type| Column Type| 
|---------|---------|---------|
|Rank|Integer||
|Pais|Intenger| RK to Paises|
|Ouro|Integer||
|Prata|Integer||
|Bronze|Integer||
|Total|Integer||
|Rank pelo Total|Integer||

Table **Times**
| Column | Attribute Type| Column Type| 
|---------|---------|---------|
|ID|Intenger|PK|
|Nome|String|
|Pais|Intenger| RK to Paises|
|Evento|Intenger|RK to Eventos|
|Jogo|Integer|RK to Jogos|

Table **Jogos**
| Column | Attribute Type| Column Type| 
|---------|---------|---------|
|ID|Intenger|PK|
|Nome|String|

Table **Eventos**
| Column | Attribute Type| Column Type| 
|---------|---------|---------|
|ID|Intenger|PK|
|Nome|String|

Table **Paises**
| Column | Attribute Type| Column Type| 
|---------|---------|---------|
|ID|Intenger|PK|
|Nome|String|
