#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:25:59 2020

@author: fernanda
"""


'''
Programa para teste do EP03
Crie outros testes que achar importantes.
Mande os seus testes para a lista de discussão.
'''

from pymagem import Pymagem

def main():
    ''' (None) -> None
    Essa função apenas testa a classe Pymagem.
    Coloque aqui outros testes que desejar.
    '''
    # testa construtor
    img1 = Pymagem(4, 5)
    img2 = Pymagem(3, 3, 88)

    print("\nChamadas da função print()")
    print("Conteúdo de img1:")
    print(img1)
    print("Conteúdo de img2:")
    print(img2)

    print("\nChamadas do método size()")
    lins1, cols1 = img1.size()
    print("Resolução de img1: %d x %d"%(lins1, cols1))
    lins2, cols2 = img2.size()
    print("Resolução de img2: %d x %d"%(lins2, cols2))

    print("\nChamadas do método crop")
    img3 = img1.crop() ## cria uma cópia
    print("Conteúdo de img3:")
    print(img3)
    img4 = img2.crop(0, 1, lins2-1, cols2)  
    print("Conteúdo de img4:")
    print(img4)

    print("\nChamadas para testar o acesso e atribuição")
    col = 2
    img1[0, col] = 11
    for lin in range(1, lins1):
        img1[lin, col] = img1[lin-1, col] + 10
    print("Conteúdo de img1:")
    print(img1)
    # não deve alterar img3
    print("Conteúdo de img3:")
    print(img3)

    # modifica a linha 1 de img2
    lin = 1
    for col in range(0, cols2):
        img2[lin, col] = 11
    print("Conteúdo de img2:")
    print(img2)
    # não deve alterar img4
    print("Conteúdo de img4:")
    print(img4)

    # mais testes inclusive os seus...
    print("Outro crop")
    print(img1.crop(1,1,3,4))
    
    #teste para subtração
    print ("subtração de img2 para matriz de 5, de mesmo tamanho:")
    print (img2 - Pymagem(img2.nlins, img2.ncols, 5))
    print ("subtração com matrizes de tamanhos diferentes:")
    print (img2 - img1)
    
    
    # teste para limiarize
    img5 = img1.crop()
    img5.limiarize(30, 100, 1)
    print (img5)
    
    # teste para erosao
    img6 = img2.crop()
    img6[2,0] = 1
    img6.erosao(3)
    print (img6)
    
    #teste para segmentacao_SME
    img7 = img2.crop()
    img7[2,0] = 1
    print ("img7 original:")
    print (img7)
    print (img7.segmentacao_SME(3))
    
if __name__ == '__main__':
    main()

