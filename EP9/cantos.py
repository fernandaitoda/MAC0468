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

import numpy as np
import cv2
import sys
import random
import math

random.seed (12345)

#-------------------------------------------------------------------------- 
# programa principal


def main ():
    global copy, gab, corners, ncorners, corners2, notDetected
    
    if len(sys.argv) != 2:
        print("Digite: python cantos.py entrada")
        return

    name = sys.argv[1]

    
    if name == '0':
        print ("AAAAAAAA")
        inpt = cv2.VideoCapture (int (name))
        _, img =  inpt.read()
        if img is None: return
        
    else:
        img = cv2.imread (name)    
        
        if img is None:
            print ("Não consegui abrir o arquivo: ", img)
            return
        
    # Exibe imagem ou captura de entrada
    cv2.imshow ("Imagem de entrada", img)
    cv2.waitKey (0)
    
    notDetected = []
    getCorners (img, 100)
    
    print (notDetected)
            
def getCorners (img, n):
    global copy, gab, corners, corners2, ncorners
    
    copy = np.copy (img)
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    
    qualityLevel = 0.01
    minDistance = 30
    
    # detection
    corners = cv2.goodFeaturesToTrack (gray, n, qualityLevel, minDistance, None, blockSize = 3, 
                                       gradientSize = 3, useHarrisDetector = False, k = 0.04)
 
    winSize = (5, 5)
    zeroZone = (-1, -1)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_COUNT, 40, 0.001)
        
    corners = cv2.cornerSubPix (gray, corners, winSize, zeroZone, criteria)
       
    # drawing
    for i in range (corners.shape[0]):
        cv2.circle (copy, (corners[i, 0, 0], corners [i, 0, 1]), 4,
                           (0, 0, 255), cv2.FILLED)
            
 
    # Exibe cantos detectados pelo opencv        
    cv2.imshow ("Cantos", copy)
        
    #muda a cor dos cantos selecionados
    gab = np.array ([])
    ncorners = 0
    cv2.setMouseCallback ("Cantos", selectCorners)
    cv2.waitKey (0)
    
    if ncorners >= 4:
        gab = np.reshape (gab, (4,2))
        final = sortGab ()
    
    # calcula altura e largura média

    h1 = distance (final[0], final[2])
    h2 = distance (final[1], final[3])
    medH = int ((h1 + h2) / 2)
    w1 = distance (final[0], final[1])
    w2 = distance (final[2], final[3])
    medW = int ((w1 + w2) / 2)
    
    # transforma imagem e salva
    dst = np.array ([
		[0, 0],
        [medW - 1, 0],
        [0, medH - 1],
        [medW - 1, medH - 1]], dtype = "float32")
    
    H = cv2.getPerspectiveTransform (final, dst)
    warp = cv2.warpPerspective (img, H, (medW, medH))

    cv2.imshow ("Imagem final", warp)            
    cv2.waitKey (0)

def selectCorners (event, x, y, flags, param):
    global copy, gab, ncorners, notDetect
    
    if event == cv2.EVENT_LBUTTONDOWN and ncorners < 4:
        x, y, change = checkNeighborhood (x, y)
        
        if change:
            notDetected.append ([x, y])
        
        else:
            cv2.circle (copy, (x, y), 4, (0, 255, 0), cv2.FILLED)   
            gab = np.append (gab, [x,y])   
            cv2.imshow ("Cantos", copy)
            ncorners += 1

def checkNeighborhood (x, y):
    global copy, corners, corners2
    
    change = True
    
    for i in range (corners.shape[0]):
        if (corners[i, 0, 0] >= x-3 and corners[i, 0, 0] <= x+3): 
            if (corners[i, 0, 1] >= y-1 and corners[i, 0, 1] <= y+3):
                x = corners[i, 0, 0]
                y = corners[i, 0, 1]
                change = False
                
            
    return x, y, change
    
def sortGab ():
    global gab
    
    sort = np.zeros((4, 2), dtype = "float32")
	
    s = gab.sum (axis = 1)
    diff = np.diff (gab, axis = 1)

    
    sort[0] = gab[np.argmin(s)]    # TL
    sort[1] = gab[np.argmin(diff)] # TR
    sort[2] = gab[np.argmax(diff)]    # BL
    sort[3] = gab[np.argmax(s)] # BR
	
    return sort    

def distance (a, b):
    distance = math.sqrt ( ( (a[0]-b[0])**2 )+( (a[1]-b[1])**2 ) )
    return distance
    
if __name__== '__main__':
    main()


