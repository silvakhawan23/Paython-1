biblioteca = {
    'titulos': {
        'A culpa é das estrelas': {
            'autor': 'John Green',
            'Ano': '2012',
            'Gênero': 'Romance',
            'Preço': '25',
            'Número de Páginas': '313',
        },
        'O Senhor dos Anéis': {
            'autor': 'J.R.R Tolkien',
            'Ano': '1954',
            'Gênero': 'Fantasia',
            'Preço': '30',
            'Número de Páginas': '1178',
        },
        'Ponto de Impacto': {
            'autor': 'Dan Brown',
            'Ano': '2001',
            'Gênero': 'Suspense',
            'Preço': '22.50',
            'Número de Páginas': '560',
        },
        'O Código da Vinci': {
            'autor': 'Dan Brown',
            'Ano': '2003',
            'Gênero': 'Suspense',
            'Preço': '24.99',
            'Número de Páginas': '689',
        },
        'A Menina que Roubava Livros': {
            'autor': 'Markus Zusak',
            'Ano': '2005',
            'Gênero': 'Ficção',
            'Preço': '18.75',
            'Número de Páginas': '584',
        }
    }
}


for titulo, info in biblioteca['titulos'].items():
    print(f'Título: {titulo}')
    print(f'Autor: {info["autor"]}')
    print(f'Ano: {info["Ano"]}')
    print(f'Gênero: {info["Gênero"]}')
    print(f'Preço: R${info["Preço"]}')
    print(f'Número de Páginas: {info["Número de Páginas"]}')
    print()

