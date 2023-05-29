# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Fernanda Itoda
    NUSP: 10740825

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

##
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

## Constantes
FUNDO = 0
DEBUG = False

def main():
    ''' 
    Carregue as imagens gere o gráfico Recall x Precision
    '''
    global blur

    if len(sys.argv) != 2:
        print("Digite: python canny.py arquivo_imagem")
        return

    fname = sys.argv[1]
    
    bname1 = "106024 (1).jpg"
    bname2 = "106024 (2).jpg"
    bname3 = "106024 (3).jpg"
    bordas = []
    
    img1 = cv2.imread (fname)
    if img1 is None:
        print ("Não consegui abrir o arquivo: ", fname)
        return
    
    img = cv2.imread (bname1)
    if img is None:
        print ("Não consegui abrir o arquivo: ", bname1)
        return
    
    bordas.append (img)
    
    img = cv2.imread (bname2)
    if img is None:
        print ("Não consegui abrir o arquivo: ", bname2)
        return    
    bordas.append (img)
    
    img = cv2.imread (bname3)
    if img[2] is None:
        print ("Não consegui abrir o arquivo: ", bname3)
        return
    bordas.append (img)
    
    gabarito = crie_gabarito (bordas)
    
    imgCinza = cv2.cvtColor (img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur (imgCinza, (5,5), 0)
    
    cv2.imshow ("Blur", blur)
    cv2.waitKey (0)
    
    array = avalie_canny (blur, gabarito)
    
    mostre_resultado (array)
## 

def mostre_resultado( array ):
    ''' (array) -> None
    Recebe um array com pares 
    '''
    rc = array.T
    plt.plot( rc[0], rc[1] )
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    plt.show()

## 

def crie_gabarito( imgs ):
    ''' (lista de imagens) -> imagem
    Constrói a imagem gabarito a partir de uma lista de imagens com
    anotações de bordas.
    ''' 
    
    #imgInv = imgs[0] + imgs[1] + imgs[2]
    imgInv = cv2.addWeighted (imgs[0], 0.5, imgs[1], 0.5, 0)
    imgInv = cv2.addWeighted (imgInv, 0.5, imgs[2], 0.5, 0)
    
    
    imgInv = cv2.cvtColor (imgInv, cv2.COLOR_BGR2GRAY)
    #imgInv = cv2.bitwise_not (imgInv)
    r, imgInv = cv2.threshold (imgInv, 127, 255, cv2.THRESH_BINARY_INV)    
    
    cv2.imshow ('GABARITO', imgInv)
    cv2.waitKey (0)
    
    return imgInv
       

def avalie_canny(blur, gab, ini=0, fim=256, passo=5, delta=60):
    ''' (imagem, imagem, int, int, int, int) -> array
    Recebe a imagem blur e um gabarito de bordas gab. 
    Deve gerar imagens de  borda usando o método de Canny para o intervalo
    de limiar inferior [ini: fim: passo]. O limiar superior do método de 
    Canny deve ser o inferior + delta. Observe que o limiar superior não deve
    ser maior que o valor de fim.
    A função retorna um numpy.ndarray com os pares (recall, precision)
    para cada par de limiares calculados.
    '''
    
    canny = cv2.Canny (blur, 60, 120) 
    
    cv2.imshow ('Canny Edges', canny)
    cv2.waitKey (0)    
    print (canny)
    
    array = []
    # 154 401
    for i in range (ini, fim, passo):
        LI = i
        LS = LI + delta
        if LS > fim:
            LS = fim
            
        edges = cv2.Canny (blur, LI, LS)
        
        #cv2.imshow ('Canny Edges', edges)
        #cv2.waitKey (0)    
        
            
        TP = np.logical_and (gab == edges, edges != 0).sum ()
        FP = np.logical_and (gab != edges, edges != 0).sum ()
        FN = np.logical_and (gab != edges, edges == 0).sum ()
        
        
        print (TP, FP, FN)
        # cv2.imshow ('ndjaksbdkslnd', edges)
        # cv2.waitKey (0)
        R = TP / (TP + FN)
        P = TP / (TP + FP)       

        #print (P, R)
        par = [R,P]
        array.append (par)
        
    ret = np.array (array)
   
    return ret
    
if __name__ == '__main__':
    main()
