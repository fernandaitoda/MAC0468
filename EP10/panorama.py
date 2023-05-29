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

import cv2
import numpy as np
import argparse

# glob pega os nomes dos arquivos em uma pasta
from glob import glob

#-------------------------------------------------------------------------- 
# programa principal

def main():

    # PARSING
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--imagens', required=True, help = "imagens de entrada como '../figs/*.png'")
    ap.add_argument('-d', '--debug', required=False, action='store_true', help = 'liga o modo debug')
    ap.add_argument('-s', '--sift', required=False,  action='store_true', help = 'usa SIFT, default é ORB')
    ap.add_argument('-sw', '--escalaW', required=False, help = 'muda a escalaW')
    ap.add_argument('-sh', '--escalaH', required=False, help = 'muda a escalaH')
    ap.add_argument('-dw', '--deltaW', required=False, help = 'posição horizontal da 1a imagem')
    ap.add_argument('-dh', '--deltaH', required=False, help = 'posição vertical da 1a imagem')
    ap.add_argument('-c', '--crosscheck', required=False, action='store_false', help = 'desliga crosscheck no cálculo de matches')
 
    args = ap.parse_args()
    print(args)

    ## SET DEFAULTS
    METODO = 'ORB'
    ESCALA_W = 3
    ESCALA_H = 3
    CROSSCHECK = True
    DELTA_W = args.deltaW   ### CUIDADO, DELTA_W é um str ou None
    DELTA_H = args.deltaH   ### CUIDADO, DELTA_H é um str ou None

    ## ATUALIZA O QUE PRECISAR
    DEBUG = args.debug
    CROSSCHECK = args.crosscheck

    if args.sift: METODO = 'SIFT'
    if args.escalaW is not None: ESCALA_W = int(args.escalaW)
    if args.escalaH is not None: ESCALA_H = int(args.escalaH)

    # AGORA VAMOS COMEÇAR

    files = glob(args.imagens)
    files = sorted(files)
    n = len(files)
    if n == 0:
        print(f"Não achei nenhuma imagem usando {files}")
        return
    else:
        print(f"Achei as seguintes {n} imagens para processar:\n")
        for i, f in enumerate( files ):
            print(f"{i} : {f}")

    # carrega 1ª imagem
    IMG_0 = cv2.imread (files[0])    
    h, w, _ = IMG_0.shape

    # cria imagem BASE 
    H = h * ESCALA_H
    W = w * ESCALA_W
    
    BASE = np.full ((H, W), 0)
    
    print (f'tamannho de BASE: {BASE.shape}')
    print (f'tamannho de IMG_0: {IMG_0.shape}')
    
    
    if args.deltaW is not None: dw = int(args.deltaW) 
    else: dw = W//4 
    if args.deltaH is not None: dh = int(args.deltaH) 
    else: dh = H//4
       
    H0 = np.eye (3)
    H0[0, 2] = dw
    H0[1, 2] = dh 
    
    BASE = cv2.warpPerspective (IMG_0, H0, (W, H))
    
    cv2.imshow ("BASE", BASE)
    
    # calcula o keypoints, descritores e matches para IMG_0
    gray_0 = cv2.cvtColor (IMG_0, cv2.COLOR_BGR2GRAY)
    
    if METODO == 'SIFT':
        metodo = cv2.SIFT_create ()
        fb = cv2.BFMatcher (cv2.NORM_L2, crossCheck = True)
    else:
        metodo = cv2.ORB_create ()
        fb = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck = True)

    kp_0, desc_0 = metodo.detectAndCompute (gray_0, None)
    
    for k in range (1, len(files)):
        IMG_k = cv2.imread (files[k])
        gray_k = cv2.cvtColor (IMG_k, cv2.COLOR_BGR2GRAY)
        kp_k, desc_k = metodo.detectAndCompute (gray_k, None)

        matches = fb.match (desc_0, desc_k)   
        matches = sorted (matches, key = lambda x: x.distance)
        
        # transforma descritores em pontos
        pts1 = np.zeros ((len(matches), 2), dtype = np.float32)
        pts2 = np.zeros ((len(matches), 2), dtype = np.float32)
        
        for i, match in enumerate (matches):
            pts1[i,:] = kp_0[match.queryIdx].pt
            pts2[i,:] = kp_k[match.trainIdx].pt
            
        # calcula homografia
        Hk, _ = cv2.findHomography (pts2, pts1, cv2.RANSAC)
        
        # transforma imagem
        pBASE = cv2.warpPerspective (IMG_k, H0@Hk, (W, H))
        BASE = np.logical_and (BASE == 0, pBASE) * pBASE + BASE
        
        if DEBUG:
            print ("Digite enter para continuar")
            k = cv2.waitKey(0)
            print (k)
            if k == 13:
                continue
     
    k = -1
    cv2.imshow ("Imagem final", BASE)
    print ("Digite enter para continuar")
    while k != 10:
        k = cv2.waitKey(0)
        if k == 13:
            break
        
    cv2.destroyAllWindows ()
        
        

if __name__== '__main__':
    main()


