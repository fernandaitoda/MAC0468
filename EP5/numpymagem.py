# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
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

#-------------------------------------------------------------------------- 

def main():
    '''
    programa para testar a classe Numpymagem
    '''

    lista = []
    k = 0
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(k)  
            k += 1
        lista.append(linha)

    img1 = Numpymagem( (), np.array(lista))  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}")

    img2 = Numpymagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}")

    print("\nChamadas do método crop")
    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}")

    img4 = img1.crop(1, 1, 5, 4)  
    print(f"img4:\n{img4}")

    img5 = img4 + img3 * 0.5
    print(f"img5:\n{img5}")

    img6 = Numpymagem( (5,5) )
    print(f"img6:\n{img6}")
    img6.paste(img5, -1, 1)
    print(f"img6 paste img5:\n{img6}")

    img7 = Numpymagem( (9, 9), 0.0)
    img8 = img7.crop()

    img7.pinte_disco(0, 8, 7, 1.1)
    print(f"teste disco:\n{img7}")

    img8.pinte_retangulo(4, -1, 8, 5, 8.8)
    print(f"teste retangulo:\n{img8}")

    print("teste disco com retangulo:")
    print(img7 + img8 * 0.5)

    ### TESTE O SEU PROGRAMA COM OUTROS EXEMPLOS
    ### PODE COLOCA-LOS NO FORUM

#-------------------------------------------------------------------------- 

class Numpymagem:
    '''
    Implementação da classe Numpymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''
    
    def __init__ (self, shape, val = 0):       
        if type (val) is int or type (val) is float:
            self.data = np.full (shape, val).copy()           
        else:
            if shape == ():
                self.data = np.reshape (val, val.shape).copy()
            else:
                self.data = np.copy (val)                
        self.shape = self.data.shape
        
    def __str__ (self):
        s = ''
        for lin in range (self.shape[0]):
            for col in range (self.shape[1]):
                if col % self.shape[1] == self.shape[1]-1:
                    s += str(self.data[lin][col]) + '\n'
                else:
                    s += str(self.data[lin][col]) + ', '
        return s 
     
    def __getitem__ (self, index):
        return self.data[index[0]][index[1]]
    
    def __setitem__ (self, index, val):
        self.data[index[0]][index[1]] = val
        
    def __add__ (self, other):
        ret = Numpymagem (self.shape)
        ret.data = np.add (self.data, other.data)
        return ret
    
    def __mul__ (self, alpha):
        ret = Numpymagem (self.shape)
        ret.data = np.multiply (self.data, alpha)
        return ret
        
    def crop (self, TLx = 0, TLy = 0, BRx = 0, BRy = 0):
        TL = (TLx, TLy)
        BR = (BRx, BRy)
                
        if BR == (0,0):
            BR = self.shape
            
        val = self.data[TL[0]:BR[0],TL[1]:BR[1]]
        return Numpymagem ((), val)
        
    def paste (self, other, tlin, tcol):
        data = self.data
        
        outlin = tlin+other.shape[0] - self.shape[0]
        outcol = tcol+other.shape[0] - self.shape[0]
        if outlin > 0: tlin2 = other.shape[0] - outlin
        else: tlin2 = other.shape[0]
        if outcol > 0: tcol2 = other.shape[1] - outcol
        else: tcol2 = other.shape[1]
        
        if tlin < 0: tlin1 = abs(tlin)
        else: tlin1 = 0
        if tcol < 0: tcol1 = abs(tcol)
        else: tcol1 = 0
        other2 = other.crop (tlin1, tcol1, tlin2, tcol2)       
        
        if tlin < 0: tlin = 0
        if tcol < 0: tcol = 0

        data[tlin:tlin+other2.shape[0], tcol:tcol+other2.shape[1]] = other2[:,:]
    
    def pinte_disco (self, lin, col, raio, valor):
        data = self.data
        
        nlin = self.shape[0]
        ncol = self.shape[1]
        
        y,x = np.ogrid[-lin: nlin-lin, -col: ncol-col]
        disco = x*x+y*y < raio*raio
        
        data[disco] = valor
        
    def pinte_retangulo (self, x, y, x2, y2, valor):
        
        val = np.full((x2-x, y2-y), valor)
        ret = Numpymagem ((), val)
        
        self.paste(ret, x, y)
        
    
    # escreva aqui os métodos da classe Numpymagem

if __name__ == '__main__':
    main()
