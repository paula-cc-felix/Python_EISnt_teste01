# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:07:47 2023

@author: paula, raquel e ricardo
"""

# Aqui está o que o jogo deve fazer:
# 1. Solicitar ao jogador que insira uma palavra para ser adivinhada.
# 2. Exibir um espaço em branco para cada letra da palavra.
# 3. Solicitar ao segundo jogador que insira uma letra.
# 4. Verificar se a letra fornecida está presente na palavra secreta.
# 5. Se a letra estiver correta, atualizar a exibição da palavra com a letra revelada.
# 6. Se a letra estiver incorreta, desenhar uma parte do boneco da forca.
# 7. Repetir os passos 3 a 6 até que o jogador adivinhe corretamente a palavra ou até que o
# boneco da forca esteja completo.
# 8. Exibir uma mensagem indicando se o jogador venceu ou perdeu o jogo.
# O número máximo de tentativas do jogador deverá ser de 5 tentativas.

# 1. Solicitar ao jogador que insira uma palavra para ser adivinhada (palavra1)
palavra1_str = input("\nJogador 1: insira a palavra a adivinhar (e não mostre ao outro jogador)\n ==> ")

palavra1_list=list(palavra1_str)
# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# print("Limpámos o ecrã para o jogador 2 não fazer batota...")

palavra2_list = [] #inicialização da palavra inserida pelo jogador 2
for posicao_letra in palavra1_list:
    palavra2_list.append("-")
palavra2_str="".join(palavra2_list) # converte a palavra2_list em palavra2_str

# 2. Exibir um espaço em branco para cada letra da palavra.
print("\nA palavra a adivinhar tem "+ str(len(palavra1_list)) + " letras\n\n" + palavra2_str)

tentativas_erradas = 0

# 7. Repetir os passos 3 a 6 até que o jogador adivinhe corretamente a palavra ou até que o boneco da forca esteja completo.
while palavra2_list != palavra1_list and tentativas_erradas <= 5:
    letra=input("Escolha uma letra\n") # 3. Solicitar ao segundo jogador que insira uma letra.
    if letra in palavra1_list:
        for posicao_letra in range(len(palavra1_list)):
            if letra == palavra1_list[posicao_letra]: # 4. Verificar se a letra fornecida está presente na palavra secreta.
                palavra2_list[posicao_letra]=palavra1_list[posicao_letra] # 5. Se a letra estiver correta, atualizar a exibição da palavra com a letra revelada.
    else:
        tentativas_erradas +=1
        print("Já errou "+ str(tentativas_erradas) +" letras. Tem mais "+str(5-tentativas_erradas) +" tentativas\n")
    palavra2_str="".join(palavra2_list)
    print(palavra2_str)
        
