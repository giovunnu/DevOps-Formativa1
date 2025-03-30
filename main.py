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
    }
}

def tipo_personagem():
    print("\n" ,"x" * 5, " OPÇÕES DE PERSONAGEM ", "x" * 5)
    print("1. GUERREIRO\n"
          "2. FAZENDEIRO\n"
          "3. POLICIAL\n"
          "4. BANDIDO\n"
          "5. PILOTO\n")
    try:
        return int(input("Escolha seu personagem (digite o número): "))
    except ValueError:
        pass

def menu_criacao ():
    print("-" * 5, " CRIE SEU PERSONAGEM ", "-" * 5)
    nick = input("Crie um nick bonito: ")
    idade = int(input("Qual a idade do seu personagem? "))
    tipo = tipo_personagem()

    if tipo in habilidades_personagem:
        categoria_personagem = {
            1: "Guerreiro",
            2: "Fazendeiro",
            3: "Policial",
            4: "Bandido",
            5: "Piloto"
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