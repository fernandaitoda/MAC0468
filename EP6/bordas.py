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

import cv2 as cv
import numpy as np
import sys

#-------------------------------------------------------------------------- 
# global vars

#-------------------------------------------------------------------------- 
# programa principal
     
def main():

    global img_cinza, borrada, sobel, norm

    if len(sys.argv) != 2:
        print("Digite: python bordas.py arquivo_imagem")
        return

    fname = sys.argv[1]
    img1 = cv.imread(fname)
    if img1 is None:
        print("Não consegui abrir o arquivo: ", fname )
        return
    
    # imagem cinza
    img_cinza = cv.cvtColor (img1, cv.COLOR_BGR2GRAY)
    
    cv.imshow ('Entrada', img1)
    cv.waitKey (0)
    
    cv.imshow ('Cinza', img_cinza)
    cv.waitKey (0)
    
    # imagem borrada
    borrada = cv.GaussianBlur (img_cinza, (3,3), 0 )
    cv.imshow ('Borrada', borrada)
    cv.createTrackbar('blurTrackbar', 'Borrada', 3, 15, trackbar_gaussiano)
    cv.waitKey (0)

    # Bordas Sobel
    gblur = cv.GaussianBlur (img_cinza, (5,5), 0 )
    sobelx = np.abs (cv.Sobel (gblur, cv.CV_64F, 1, 0, ksize = 5))
    sobely = np.abs (cv.Sobel (gblur, cv.CV_64F, 0, 1, ksize = 5)) 
    
    sobelxy = np.hypot (sobelx, sobely)
    sobel = np.zeros (sobelxy.shape, dtype='uint8')
    sobel = cv.normalize (sobelxy, sobel, 0, 255, norm_type=cv.NORM_MINMAX, dtype = cv.CV_8UC1)
    
    valor = 70
    r, imgBinxy = cv.threshold (sobel, valor, 255, cv.THRESH_BINARY)
    
    cv.imshow ('Bordas Sobel', imgBinxy)
    cv.createTrackbar ('SobelTrackbar', 'Bordas Sobel', valor, 255, trackbar_sobel)
    cv.waitKey (0)
    
    # Bordas Laplace
    # ddepth = cv.CV_16S
    # laplace = cv.Laplacian (gblur, ddepth, ksize = 5)
    # norm = np.zeros (laplace.shape, dtype='uint8')
    # norm = cv.normalize (laplace, norm, 0, 255, norm_type=cv.NORM_MINMAX, dtype = cv.CV_8UC1)
    
    # val = 40
    # ret, imB = cv.threshold (norm, val, 255, cv.THRESH_BINARY)
    # cv.imshow ('Bordas Laplace', imB)
    # cv.createTrackbar ('LapTrackbar', 'Bordas Laplace', val, 255, trackbar_laplace)
    # cv.waitKey (0)
    
    # resto do seu programa
    
def trackbar_gaussiano (valor):
        global img_cinza
        #alfa = valor / MAXVALOR
        #beta = 1 - alfa
        borrada = cv.GaussianBlur (img_cinza, (valor,valor), 0)
        #res = beta * img_cinza + alfa * img_gaussiano
        #m = np.max (res)
        #res = res * (1/m)
        cv.imshow ('Borrada', borrada)
        
def trackbar_sobel (valor):
        global sobel
        r, imgBinxy = cv.threshold (sobel, valor, 255, cv.THRESH_BINARY)
        cv.imshow ("Bordas Sobel", imgBinxy)

# def trackbar_laplace (valor):
#         global norm
#         ret, imB = cv.threshold (norm, valor, 255, cv.THRESH_BINARY)
#         cv.imshow ('Bordas Laplace', imB)
    
if __name__== '__main__':
    main()

