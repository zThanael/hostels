<h1> Como encontrar Hostels pelo Mundo 🌍</h1>
<p> Como descobrir os hostels de uma localidade e planejar sua viagem.</p>

<hr>

<h3> Sumário </h3>
<ul>
    <li> <a href='info'> Informações Gerais </a>
        <ul>
            <li> <a href='#contexto'> Contexto </a> </li>
            <li> <a href='#problema'> Problemática </a> </li>
            <li> <a href='#objetivo'> Objetivo </a> </li>
        </ul>
    </li>
    <li> 
        <a href='#desenvolvimento'> Desenvolvimento </a>
        <ul>
            <li> <a href='#pipeline'> Data Pipeline  </a> </li>
            <li> <a href='#etl'> ETL </a> </li>
            <li> <a href='#der'> DER </a> </li>
            <li> <a href='#visualizacao'> Visualizações </a> </li>
        </ul>
    </li>
</ul>

<hr>

<br>

<h2 id='info'> Informações Gerais  </h2>
<p>
    Aqui estão as informações básicas para compreender melhor o escopo deste projeto, bem como sua finalidade.
</p>

<hr>

<h3 id='contexto'> Contexto </h3>
<p> 
    Muitos não sabem mas além de Analista de Dados eu também sou Nômade Digital, mas o que isso significa ? Que estou sempre viajando para novos lugares enquanto continuo trabalhando remotamente. 
</p>
<p>
    Existem algumas abordagens sobre hospedagem para quem busca este estilo de vida nômade, uma delas a qual eu utilizo é a de se hospedar em Hostels. 
</p>
<p>
    Hostels são albergues de baixo custo no qual você convive com mais pessoas no mesmo ambiente, eles são muito buscados por jovens viajantes de todos os lugares do mundo. Portanto é comum encontrar pessoas de outros países em Hostels.  
</p>

<hr>

<h3 id = 'problema'> Problemática </h3>

<p>
    Uma dificuldade comum de quem possui este estilo de vida consiste na dificuldade de pesquisar pelos Hostels que pretende se hospedar.
</p>
<p>
    Algumas das formas mais comuns de procurar por Hostels são:
</p>
<ul>
    <li> 
    <a href=''> HostelWorld </a>: Na minha opinião é o site mais utilizado para pesquisar por hostels. 
    </li>
    <li> 
    <a href=''> Instagram </a>: Mesmo não sendo a mais usada ainda é muito útil para pesquisar por hostels.
    </li>
    <li>
    <a href=''> Google e Maps </a>: É comum abrirmos o Maps e pequisar por Hostel na cidade que desejos se hospedar.
    </li>
</ul>
<p>
    Mesmo o HostelWorld sendo a mais utilizada ainda é dificil e maçante descobrir quais os hostels existem em determinado local.
</p>
<p>
    Por exemplo, estou planejando minhas viagens para o Peru, e é dificil descobrir quais cidades possuêm hostels, principalmente no HostelWorld pois precisa por a cidade e datas. Mas meu objetivo é descobrir quais cidades do Peru possuem hostels...
</p>

<hr>

<h3 id = 'objetivo'> Objetivo </h3>
<p>
    <b> Facilitar a vida de quem procura por Hostels, no caso a minha própria 😅.</b>
</p>
<p>
    Criando uma forma simples de pesquisar por hostels, ao colocar um país/cidade obter todos os hostels que existem naquela localização.
</p>

<hr>

<br>

<h2 id='info'> Desenvolvimento  </h2>
<p>
    Nesta seção entrará o conteúdo mais técnico explicando como será resolvido o problema e criado a solução. Portanto aqui entrará temas mais técnicos sobre a área de dados. 
</p>

<hr>

<h3 id='pipeline'> Data Pipeline  </h3>
<p>
    Segue abaixo a arquitetura do pipeline de dados referente a este projeto.
</p>
<img src='pipeline.png'>
<p>
    Os dados foram obtidos do Kaggle e as tratativas foram realizados através de uma ETL em Python para alimentar o Data Warehouse que consiste em um PostgreSQL instânciado em um RDS na AWS. 
</p>
<p>
    Sobre a utilização dos dados será confecionado um dashboard interativo no Streamlit com deploy em Cloud.
</p>

<hr>

<h3 id = 'etl'> ETL - Extract, Transform and Load</h3>
<ul>
    <li>  
        <b> Extract </b>: Os dados usados para este projeto foram obtidos do Kaggle em: <a href='https://www.kaggle.com/datasets/felipejardimf/hotel-reviews-hostelworld'> Hotel Reviews - Hostelworld </a> 
    </li>
    <br>
    <li> 
        <b> Transform </b>: Os dados crus não são adequados para o nosso objetivo, portanto foi necessário realizar as tratativas nos dados e principalmente criar a modelagem mais adequada para o Projeto <br>
        <i> Todo o processo foi documentado em <a href='https://github.com/zThanael/hostels/blob/main/etl_hostel.ipynb'> etl_hostel.ipynb </a> </i>
    </li>
    <br>
    <li> 
        <b> Load </b>: Após as devidas transformações nos dados eles foram inseridos em um Banco PostgreSQL instânciado em um RDS na AWS
    </li>

</ul>
<hr> 

<h3 id = 'der'> DER - Diagrama de Entidade e Relacionamentos </h3>
<p>
    A modelagem dos dados consite em: 
</p>
<img src='DER.png'>
<p> 
    Como a tabela principal <b> hostelworld_hostel </b> possui poucos dados (40.000) e não aumentará mais, não vejo a necessidade de normaliza-la.
</p>
<p> 
    Porém, em relação as facilidades de cada Hostel precisei normalizar os dados devido a quantidade, portanto para otimizar o armazenamento dos dados e o desempenho visto que estou usando o Free Tier da AWS, normalizei a tabela <b> hostelworld_hostel_facilities </b> ( <b>880.000 registros </b>) transformando-a em uma tabela fato similar a arquitetura <b> Star Schema </b>.
</p>

<hr>

<h3 id = 'visualizacao'> Visualizações </h3>
<p> 
    Para as visualizações, foi utilizado o <b> Streamlit </b> para criação de uma aplicação web na qual é possível navegar e descobrir os hostels existentes pelo mundo todo.
</p>
<blockquote> O código criado no Streamlit está em outro repositório, fazendo parte de um produto. </blockquote>
<p> 
    Segue abaixo imagens desta aplicação.
</p>
<ul>
    <li> Tela Principal: <br>
        <img src='search_hostel_1.png'>
    </li>
    <li> Listagem: <br>
        <img src='search_hostel_2.png'>
    </li>
    <li> Visão de Pais: <br>
        <img src='search_hostel_3.png'> 
    </li>
</ul>