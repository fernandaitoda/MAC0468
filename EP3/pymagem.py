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

#-------------------------------------------------------------------------- 

class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''
    
    def __init__ (self, nlins, ncols, valor = 0):
        self.nlins = nlins
        self.ncols = ncols
        
        data = []
        for lin in range (nlins):
            data.append ([])
            for col in range (ncols):
                data[lin].append (valor)        
        self.data = data
    
    def __str__ (self):
        s = ''
        for lin in range (self.nlins):
            for col in range (self.ncols):
                if col % self.ncols == self.ncols-1:
                    s += str(self.data[lin][col]) + '\n'
                else:
                    s += str(self.data[lin][col]) + ', '
        return s 
    
    def __getitem__ (self, index):
        return self.data[index[0]][index[1]]
    
    def __setitem__ (self, index, valor):
        self.data[index[0]][index[1]] = valor
        
    def __sub__ (self, mat):
        if self.size() == mat.size():
            ret = Pymagem (self.nlins, self.ncols)
            for lin in range (self.nlins):
                for col in range (self.ncols):
                    ret[lin,col] = self[lin,col] - mat[lin,col]
            return ret
        else:
            print ("Matrizes com dimensões diferentes.")
            return None
        
    def size (self):
        size = (self.nlins, self.ncols)
        return size
    
    def crop (self, top_lin = 0, top_col = 0, bottom_lin = None, bottom_col = None):
        if bottom_lin == None:
            bottom_lin = self.nlins
        if bottom_col == None:
            bottom_col = self.ncols
            
        new = Pymagem (bottom_lin - top_lin, bottom_col - top_col)
        for lin in range (top_lin,bottom_lin):
            for col in range (top_col,bottom_col):
                new[lin-top_lin, col-top_col] = self[lin,col]
        return new
    
    def limiarize (self, limite, alto, baixo):
        for lin in range (self.nlins):
            for col in range (self.ncols):
                if self[lin,col] > limite:
                    self[lin,col] = alto
                else:
                    self[lin,col] = baixo
    
    def erosao (self, viz):
        clone = self.crop()
        med = int(viz/2)
        
        for lin in range (self.nlins):
            for col in range (self.ncols):
                # checagem dentro da vizinhança
                for vi in range (lin-med, lin+med+1):
                    for vj in range (col-med, col+med+1):
                        if 0 <= vi < self.nlins and 0 <= vj < self.ncols:
                            if clone[vi,vj] < self[lin,col]:
                                self[lin,col] = clone[vi,vj]

    def segmentacao_SME (self, viz):
        ero = self.crop ()
        ero.erosao (viz)
        ret = Pymagem (self.nlins, self.ncols)
        
        for lin in range (self.nlins):
            for col in range (self.ncols):
                ret[lin,col] = self[lin,col] - ero[lin,col]
                
        return ret
        