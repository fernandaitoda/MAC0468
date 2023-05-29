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
from numpymagem import Numpymagem
from numpymutil import mostre_video
from numpymutil import salve_video
from random import randint

# Escreva aqui outras constantes que desejar
ALTURA  = 120
LARGURA = 160
BLACK = 0
WHITE = 250

#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    
        
    img = Numpymagem( (10, 10), 10)
    print(type(img.data) is np.ndarray)
        
    video = []
    preto = Numpymagem( (ALTURA, LARGURA), BLACK)    
    # branco = Numpymagem( (ALTURA, LARGURA), WHITE)
    print(f"Está compatível com numpymutil: {type(preto.data) is np.ndarray}")
    # cor = BLACK

    # mostre = True
    # if mostre:
    #     mostre_video(video)

    salve = False
    if salve:
        print("Salvando vídeo")
        salve_video(video)

#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
    
     
    # número de imagens
    no_imagens = 300
    
    # o vídeo terá no_imagens 'frames'=Numpymagem
    video = [None] * no_imagens   
    mostre = True
        
    MRet = 80
    PRet = 60
    retL = 20
    retC = 60
    ret2L = 30
    ret2C = 40
    
    linDisco = retL + 3
    colDisco = retC + 3
    
    goback = False
    ret2 = False       
    complete = False
    
    alfa = 0.0
    
    third = False
    end = False
    lin = 10
    
    for i in range (no_imagens):

        if third == False:
            img = Numpymagem ((ALTURA, LARGURA), BLACK)
            img.pinte_retangulo (retL, retC, retL+MRet, retC+PRet, WHITE)
            img.pinte_retangulo (retL+5, retC+5, retL+MRet-5, retC+PRet-10, BLACK)
                       
            if ret2 == True:
                img.pinte_retangulo (ret2L, ret2C, ret2L+PRet, ret2C+MRet, WHITE)
                img.pinte_retangulo (ret2L+5, ret2C+5, ret2L+PRet-5, ret2C+MRet-5, BLACK)
            
            if (img[[linDisco, colDisco]] == BLACK):
                img.pinte_disco (linDisco, colDisco, 4, WHITE)
            else:
                img.pinte_disco (linDisco, colDisco, 4, BLACK)
            if goback == False:
                if complete == True and colDisco >= (retC+97)/2:
                    if linDisco < (retL+97)/2:
                        linDisco += 2

                elif colDisco < 97:
                    colDisco += 2
                elif linDisco < 97:
                    linDisco += 2
                else:
                    ret2 = True
                    goback = True
            else:
                if colDisco > 63:
                    colDisco -= 2
                elif linDisco > 23:
                    linDisco -= 2
                else:
                    ret2 = False
                    goback = False
                    complete = True
        if i <= no_imagens-50:    
            img2 = Numpymagem ((ALTURA, LARGURA), BLACK)
            for j in range (30):
                if i % 2 == 0:
                    raio = i%100
                img2.pinte_disco(ALTURA//2+randint(0,20)-randint(0,20), LARGURA//2+randint(0,20)-randint(0,20), raio, randint(0,256))
          
        if third == False and i > 100:
            alfa += 0.01
            if alfa >= 1:
                third = True
                first = True
                
        if third == True and end == False:
            if alfa > 0:
                alfa -= 0.1
            else:
                alfa = 0.0
            if first == True:
                goback = False
                cor = BLACK
                bgColor = WHITE
                first = False
                        
            img = Numpymagem((ALTURA, LARGURA), bgColor)
        
            for col in range (10,LARGURA,10):
                img.pinte_disco (lin, col, 5, cor)
            if goback == False and lin < ALTURA-2*5-1:
                lin += 2
            else:
                lin -= 2
                goback = True
            
            for col in range (10,LARGURA,10):
                img.pinte_disco (ALTURA-lin, col, 5, cor)
            if goback == False and lin < ALTURA-2*5-1:
                lin += 2
            else:
                lin -= 2
                goback = True
        
        if i > no_imagens-70:
            if i <= no_imagens-49:
                alfa = 1
                img2 = Numpymagem ((ALTURA, LARGURA), WHITE)
                raio = 100
                end = True
                
            for j in range (30):
                if i % 2 == 0:
                    raio -= 2
                    if raio < 0:
                        raio = 1
                img2.pinte_disco(ALTURA//2+randint(0,20)-randint(0,20), LARGURA//2+randint(0,20)-randint(0,20), raio, randint(0,256))
                        
        video[i] = img * (1-alfa) + img2 * alfa
        
    if mostre:
        mostre_video(video) # função do módulo numpymutil
        
        


#
#-------------------------------------------------------------------------- 


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()