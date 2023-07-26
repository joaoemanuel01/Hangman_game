# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Imoprt
import random
from os import system, name

# Função para limpar a tela a cada execução 
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')


# Função que desenha a forca na tela
def display_hangmam(chances):

    # Lista de estágios da forca
    stages = [ # Estágio 6(final)
               """
                  --------  
                  |      |
                  |      O
                  |     \\|/
                  |      | 
                  |     / \\
                  -
               """,

               # Estágio 5
               """
                  --------  
                  |      |
                  |      O
                  |     \\|/
                  |      | 
                  |     / 
                  -
               """,

               # Estágio 4
               """
                  --------  
                  |      |
                  |      O
                  |     \\|/
                  |      | 
                  |     
                  -
               """,

               # Estágio 3 
               """
                  --------  
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
               """,

               # Estágio 2
               """
                  --------  
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
               """,

               # Estágio 1
               """
                  --------  
                  |      |
                  |      O
                  |      
                  |      
                  |     
                  -
               """,

                 # Estágio 0
               """
                  --------  
                  |      |
                  |      
                  |      
                  |      
                  |     
                  -
               """,
    ]
    return stages[chances]

# Função do jogo

def game():
    limpa_tela() 

    print("\nBem vindo ao jogo da forca!")
    print("O tema é: Frutas")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras do jogo
    palavras = ['banana', 'abacate', 'uva', 'laranja', 'graviola', 'melancia', 'abacaxi', 'goiaba']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # Lists de palavras
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro 
    tabuleiro = ["_"] * len(palavra)

    # Número de chances 
    chances = 6

    # Lista para as letras digitadas
    letras_tentativas = []

    # Loop enquanto o número de chances for maior que zero
    while chances > 0:

        print(display_hangmam(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentativa
        tentativa = input("\nDigite uma letra: ")

        # Condicional
        if tentativa in letras_tentativas:
            print("Você ja tentou essa letra. Escolha outra!")
            continue

        # Lista de tentativas(letras)
        letras_tentativas.append(tentativa)

        # Condicional
        if tentativa in lista_letras_palavras:

            print("Você acertou a letra!")

            # Loop 
            for indice in range(len(lista_letras_palavras)):

                # Condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            # Se todos os espaços foram preenchidos o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                break
        else:
            print("Ops. Essa letra não esta na palavra!")
            # Decremento
            chances -= 1 
    
    # Condicional 
    if "_" in tabuleiro:
     print("\nVocê perdeu! A palavra era: {}.".format(palavra))


# Bloco main
if __name__ == "__main__":
    game()