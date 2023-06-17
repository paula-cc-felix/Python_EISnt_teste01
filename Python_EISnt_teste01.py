# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:07:47 2023

@author: paula, raquel e ricardo
"""
import random

# Início do jogo

print("\n\nOlá! Vamos jogar uma versão diferente do jogo da forca!\n")
print("Em vez de salvar um homenzinho de ser pendurado pelo pescoço, desta vez o objectivo é evitar a destruição do Templo de Diana, em Évora.\n")
print("Oh para ele aqui tão lindo! Que obra de arte!\n")

# Desenho do Templo de Diana
templo=[0,1,2,3,4,5]
templo[0]=" ____________________________________\n_\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/_\n  ||      ||      ||      ||      ||\n  ||      ||      ||      ||      ||\n  ||      ||      ||      ||      ||\n  ||      ||      ||      ||      ||\n  ||      ||      ||      ||      ||\n  ||      ||      ||      ||      ||\n  ||      ||      ||      ||      ||\n"
templo[1]=" ____________________________________\n_\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/_\n  ||      ||              ||      ||\n  ||      ||              ||      ||\n  ||      ||              ||      ||\n  ||      ||              ||      ||\n  ||      ||              ||      ||\n  ||      ||              ||      ||\n  ||      ||              ||      ||\n"
templo[2]=" ____________________________________\n_\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/_\n  ||                      ||      ||\n  ||                      ||      ||\n  ||                      ||      ||\n  ||                      ||      ||\n  ||                      ||      ||\n  ||                      ||      ||\n  ||                      ||      ||\n"
templo[3]=" ____________________________________\n_\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/_\n  ||                              ||\n  ||                              ||\n  ||                              ||\n  ||                              ||\n  ||                              ||\n  ||                              ||\n  ||                              ||\n"
templo[4]=" ____________________________________\n_\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/_\n  ||                                \n  ||                                \n  ||                                \n  ||                                \n  ||                                \n  ||                                \n  ||                                \n"
templo[5]="\nVocê perdeu! Fué fué fué fué...\nE é responsável pela destruição de um monumento nacional,\nPatrimónio Mundial da UNESCO!\n\n   __      |--\/\/      \n_   |-\//   ||  _\/\/    --  |\n   -\\/   \/\/|    ||\/\/    |\n"

tentativas_erradas = 0
print(templo[tentativas_erradas])
print("\n\nPode errar 4 letras, à 5ª tentativa errada o Templo vai abaixo!")
print("\n\nVamos testar essa geografia. Conhece todas as capitais europeias?...\n")

# 1. escolha aleatoria da palavra a partir de uma lista

palavras_lista = ['Amesterdao','Atenas','Bacu','Belfast','Belgrado','Berlim','Berna','Bratislava','Bruxelas','Bucareste','Budapeste','Cardiff','Copenhaga','Dublin','Edimburgo','Estocolmo','Helsinquia','Kiev','Londres','Luxemburgo','Madrid','Minsk','Moscovo','Oslo','Paris','Praga','Reykjavik','Riga','Roma','Sarajevo','Sofia','Tallinn','Tiblissi','Tirana','Vaduz','Valeta','Varsovia','Viena','Vilnius','Zagreb']
palavra1_str = random.choice(palavras_lista).upper()
palavra1_list=list(palavra1_str)

palavra2_list = [] # inicialização da palavra (lista de letras) inserida pelo jogador

for posicao_letra in palavra1_list:
    palavra2_list.append("-")
palavra2_str="".join(palavra2_list) # converte a palavra2_list em palavra2_str

# 2. Exibir um espaço em branco para cada letra da palavra.
print("\nA capital europeia a adivinhar tem "+ str(len(palavra1_list)) + " letras\n\n" + palavra2_str)


# 7. Repetir os passos 3 a 6 até que o jogador adivinhe corretamente a palavra ou até que o boneco da forca esteja completo.
while palavra2_list != palavra1_list and tentativas_erradas < 5:
    letra=input("\nEscolha uma letra\n-> ").upper() # 3. Solicitar ao jogador que insira uma letra.
    if letra in palavra1_list:
        for posicao_letra in range(len(palavra1_list)):
            if letra == palavra1_list[posicao_letra]: # 4. Verificar se a letra fornecida está presente na palavra secreta.
                palavra2_list[posicao_letra]=palavra1_list[posicao_letra] # 5. Se a letra estiver correta, atualizar a exibição da palavra com a letra revelada.
    else:
        print("== " + letra + " == não consta desta palavra")
        tentativas_erradas +=1
        print(templo[tentativas_erradas]) # 6. Se a letra estiver incorrecta, desenhar uma parte do boneco
        if tentativas_erradas < 5:
            print("Já errou "+ str(tentativas_erradas) +" letras. Pode errar mais "+str(4-tentativas_erradas) +" letras\n")
        else:
            print("Ah, é verdade! A capital era "+palavra1_str)
            break
    palavra2_str="".join(palavra2_list)
    print(palavra2_str)
        
if palavra2_list == palavra1_list:
    print("Parabéns!!! Voce é um vencedor!!!\n") # 8. Exibir uma mensagem indicando se o jogador venceu o jogo
