Catálogo de Livros

1. Integrantes da dupla

Integrante 1: Francisco Guilherme Alves Elias
Integrante 2: Luma Maria Andrade Bandeira

2. Tema escolhido

O tema escolhido foi o Catálogo de Livros, desenvolvido com Django e Python.
O projeto Catálogo de Livros tem como objetivo organizar e disponibilizar informações sobre livros, permitindo que os usuários consultem obras literárias, pesquisem e filtrem os resultados por autor, título e gênero literário.
Além de o sistema apresentar informações detalhadas de cada livro, como gênero, ano de publicação, título, autor e descrição.

3. Filtros implementados

A listagem de livros possui três formas de pesquisa e filtragem:

3.1. Pesquisa por título

Permite pesquisar livros pelo título, pela consulta icontains, responsável por localizar resultados mesmo quando o usuário informa apenas uma letra ou parte do nome.

3.2. Filtro por gênero literário

Permite selecionar um gênero e apresentar somente os livros correspondente aquele gênero.

3.3. Filtro por autor

Permite selecionar um autor determinado e ver somente os livros correspondentes a ele.

3.4. Combinação de filtros

Os filtros podem ser utilizados concomitantemente. Desse modo, é possível pesquisar um título limitar as escolhas.

3.5. Ordenação

Os livros são organizados em ordem alfabética crescente, de acordo com o título.

4. Paginação

O catálogo utiliza o recurso Paginator do Django para dividir os resultados em páginas.

Foram implementadas as seguintes características:

Exibição de 5 livros por página.
Botão para avançar para a próxima página.
Botão para retornar à página anterior.
Indicação da página atual e da quantidade total de páginas.
Preservação dos filtros e dos termos de pesquisa durante a navegação entre as páginas.
A paginação facilita a consulta quando existe uma quantidade maior de livros cadastrados.

5. Captura de tela

   <img width="1892" height="900" alt="image" src="https://github.com/user-attachments/assets/ca537f65-79bc-447b-b5aa-c7bb87493c21" />

   <img width="1857" height="901" alt="image" src="https://github.com/user-attachments/assets/c30f83d1-18cd-4b1f-ac3c-d48c38d24b3e" />

   <img width="1862" height="902" alt="image" src="https://github.com/user-attachments/assets/1b35bc5b-4c25-4a26-8806-ce61f6fad4d7" />

   <img width="1886" height="768" alt="image" src="https://github.com/user-attachments/assets/4c3df22f-8819-4c7d-9b4d-6f7307cb98c6" />


