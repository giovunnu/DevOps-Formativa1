#Joguinho de sobrevivência

import time
from traceback import print_tb

habilidades_personagem = {
    1:{ #Guerreiro
        "Habilidades" : ["Soco Forte", "Chute Rápido", "Defesa de Ferro"],
        "Força" : 5,
        "Velocidade" : 2
    },
    2:{ #Fazendeiro
        "Habilidades" : ["Comida Infinita", "Resistência ao Sol", "Defesa com Animais"],
        "Força" : 3,
        "Velocidade" : 3
    },
    3:{ #Policial
        "Habilidades" : ["Tiro Preciso", "Agilidade", "Autodefesa"],
        "Força" : 2,
        "Velocidade" : 5
    },
    4:{ #Bandido
        "Habilidades" : ["Furtividade", "Negociação", "Defesa com Socos"],
        "Força" : 3,
        "Velocidade" : 4
    },
    5:{ #Piloto
        "Habilidades" : ["Navegação", "Manobras Insanas", "Foge para se Defender"],
        "Força" : 1,
        "Velocidade" : 4
    },
    6:{ #Encanador
        "Habilidades" : ["Fugir pelos canos", "Ser muito fino", "Espancar para se defender"],
        "Força" : 2,
        "Velocidade" : 5
    }
}

def tipo_personagem():
    while True:
        print("\n" + "x" * 5, " OPÇÕES DE PERSONAGEM ", "x" * 5)
        print("1. GUERREIRO\n"
              "2. FAZENDEIRO\n"
              "3. POLICIAL\n"
              "4. BANDIDO\n"
              "5. PILOTO\n"
              "6. ENCANADOR\n")
        try:
            escolha = int(input("Escolha seu personagem (digite o número): "))
            if 1 <= escolha <= 6:
                return escolha
            else:
                print("Opção inválida! Escolha um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida! Digite apenas números entre 1 e 6.")

def menu_criacao ():
    print("-" * 5, " CRIE SEU PERSONAGEM ", "-" * 5)
    nick = input("Crie um nick bonito: ").upper()
    idade = int(input("Qual a idade do seu personagem? "))
    tipo = tipo_personagem()

    if tipo in habilidades_personagem:
        categoria_personagem = {
            1: "Guerreiro",
            2: "Fazendeiro",
            3: "Policial",
            4: "Bandido",
            5: "Piloto",
            6: "Encanador"
        }
        categ_personagem = categoria_personagem[tipo]
        print(f"\nInteressante! O seu personagem é {categ_personagem}")
        personagem = habilidades_personagem[tipo]
        print(f"\nBem-vindo(a) {nick}"
              f"\nEsse jogo é bastante desafiador!"
              f"\n{idade} anos de experiência? Uau!")
        time.sleep(2)
        print("\nHmmm... deixa eu pensar...")
        time.sleep(2)
        print(f"\nAh, sim... seu personagem já nasceu com algumas habilidades, veja:\n")
        print(f"Habilidades: {', '.join(personagem['Habilidades'])}")
        print(f"Força: {personagem['Força']}")
        print(f"Velocidade: {personagem['Velocidade']}")
    else:
        print("Opção inválida. Tente novamente")

menu_criacao()