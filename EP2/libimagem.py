# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
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

import ep01 

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    # coloque aqui os seus testes

    mat = [ [1] ]
    print( ep01.to_string(mat, 'Olá Mundo!!') )

    # Testes do EP01
    maux = [ [1,2,3,4,5],[3,4,5,6,7],[2,4,6,8,1],[5,3,1,7,9],[9,6,3,1,7] ]
    print( 'Matriz maux:')
    print( maux )
    print()
    print( ep01.to_string(maux, '> maux' ) )

    nova = ep01.crie (5, 5, 10)
    print( ep01.to_string( nova, '> nova') )

    dif = ep01.subtraia( nova, maux)
    print( ep01.to_string( dif , '> dif = nova - maux') )

    clo = ep01.clone(dif)
    print( ep01.to_string( clo , '> clo') )

    ep01.limiarize(clo, 5)
    print( ep01.to_string( clo , '> clo apos limiarize') )

    print( ep01.to_string( dif , '> dif apos limiarize') )

    ## Testes EP02
    M = [[9,4,5,0,8],[10,3,2,1,7],[9,1,6,3,15],[0,3,8,10,1],[1,16,9,12,7]]
    print (ep01.to_string (M, '> Matriz M:'))

    ero = ep01.clone (M)  
    dil = ep01.clone (M)
    
    erosao (ero)
    print (ep01.to_string (ero, '> M após erosão'))

    segSME = segmentacao_SME (M)
    print (ep01.to_string (segSME, '> M após segmentação SME'))
    
    
    dilatacao (dil)
    print (ep01.to_string (dil, '> M após dilatação'))
    
    M = [[9,4,5,0,8],[10,3,2,1,7],[9,1,6,3,15],[0,3,8,10,1],[1,16,9,12,7]]
    segSDM = segmentacao_SDM (M)
    print (ep01.to_string (segSDM, '> M após segmentação SDM'))
    
    ## 

#------------------------------------------------------------------
#
def erosao ( img, viz = 3 ):
    ''' (matriz, int) -> None

    RECEBE uma matriz `img` representando uma imagem em níveis de cinza e
    um inteiro `viz`.

    MODIFICA `img` de tal forma que, ao final, cada pixel 
    [lin][col] seja o valor mínimo da vizinhança de tamanho `viz`
    centrada no pixel [lin][col] da imagem original.

    Pré-condição: a função supõe que `viz` é um número ímpar 
    positivo.
    '''
    
    clone = ep01.clone(img)
    med = int(viz/2)
    
    nlins = len(img)
    ncols = len(img[0])
    
    for i in range (nlins):
        for j in range (ncols):
            # checagem dentro da vizinhança
            for vi in range (i-med, i+med+1):
                for vj in range (j-med, j+med+1):
                    if 0 <= vi < nlins and 0 <= vj < ncols:
                        if clone[vi][vj] < img[i][j]:
                            img[i][j] = clone[vi][vj]

#------------------------------------------------------------------
#
def segmentacao_SME( img, viz = 3 ):
    ''' (matriz, int) -> matriz

    RECEBE uma matriz `img`. 
    APLICA o filtro de erosão com vizinhança viz.
    RETORNA a imagem resultado da subtração entre `img` e sua erosão. 
    Veja exemplos no enunciado.
    '''
    
    nlins = len(img)
    ncols = len(img[0])
    ero = ep01.clone (img)
    erosao (ero, viz)
    ret = ep01.crie(nlins, ncols)
    
    for i in range (nlins):
        for j in range (ncols):
            ret[i][j] = img[i][j] - ero[i][j]
            
    return ret

#------------------------------------------------------------------
#
def dilatacao ( img, viz = 3 ):
    ''' (list, int) -> None
    recebe uma imagem img (lista de listas) em níveis de cinza e
    um inteiro viz.

    A função modifica img tal que, ao final, cada pixel 
    img[lin][col] deve ser substituido pelo valor máximo da vizinhança de
    tamanho viz x viz centrado no pixel (lin,col) da imagem original. 
    Observe que essa região é menor quando o pixel (lin,col) 
    está em um canto ou perto de uma borda.

    Você pode assumir que viz será sempre um número ímpar, que define
    um quadrado centrado em um ponto (lin,col) de lado tam.
    '''
    
    clone = ep01.clone(img)
    med = int(viz/2)
    
    nlins = len(img)
    ncols = len(img[0])
    
    for i in range (nlins):
        for j in range (ncols):
            # checagem dentro da vizinhança
            for vi in range (i-med, i+med+1):
                for vj in range (j-med, j+med+1):
                    if 0 <= vi < nlins and 0 <= vj < ncols:
                        if clone[vi][vj] > img[i][j]:
                            img[i][j] = clone[vi][vj]
    

#------------------------------------------------------------------
#
def segmentacao_SDM( img, viz = 3 ):
    ''' (list, int) -> list
    RECEBE uma imagem img. 
    APLICA o filtro de dilatação com vizinhança viz.
    RETORNA a imagem resultado da subtração entre a dilatação e img. 
    Veja exemplos no enunciado.
    '''
    
    nlins = len(img)
    ncols = len(img[0])
    dil = ep01.clone (img)
    dilatacao (dil, viz)
    ret = ep01.crie(nlins, ncols)
    
    for i in range (nlins):
        for j in range (ncols):
            ret[i][j] = dil[i][j] - img[i][j]
            
    return ret

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
