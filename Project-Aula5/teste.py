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

def imprimir_livro(titulo, info):
    print("\033[96m" + f'Título: {titulo}' + "\033[0m")  # Cor ciano
    print(f'Autor: {info["autor"]}')
    print(f'Ano: {info["Ano"]}')
    print("\033[92m" + f'Gênero: {info["Gênero"]}' + "\033[0m")  # Cor verde
    print(f'Preço: R${info["Preço"]}')
    print(f'Número de Páginas: {info["Número de Páginas"]}')
    print('-' * 30)

def menu():
    while True:
        print("\033[92m" + "Biblioteca de Livros" + "\033[0m")  # Cor verde
        print("Escolha um livro para ver as informações (ou 's' para sair):")
        for i, titulo in enumerate(biblioteca['titulos']):
            print("\033[93m" + f"{i + 1}. {titulo}" + "\033[0m")  # Cor amarela

        escolha = input("\033[95m" + "Opção: " + "\033[0m")  # Cor magenta

        if escolha == 's':
            break
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(biblioteca['titulos']):
                titulo = list(biblioteca['titulos'].keys())[escolha - 1]
                info = biblioteca['titulos'][titulo]
                imprimir_livro(titulo, info)
            else:
                print("\033[91m" + "Escolha inválida. Tente novamente." + "\033[0m")  # Cor vermelha
        except ValueError:
            print("\033[91m" + "Escolha inválida. Tente novamente." + "\033[0m")  # Cor vermelha

menu()
