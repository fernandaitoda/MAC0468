"""
Funções para auxiliar na avaliação do seu método de 
cálculo dos limiares para o método e Canny.
"""
import cv2
import matplotlib.pyplot as plt

##  -----------------------------------------------------------------

def mostre_resultado( d ):
    ''' (dict) -> None
    Recebe um array com pares 
    '''
    x = []
    y = []
    c = 0
    for i in sorted(d.keys()):
        x.append(f"{i[0]}{c}" )
        y.append(d[i])
        c+=1
    plt.plot( x, y )
    plt.xlabel('Imagem')
    plt.ylabel('F-score')
    plt.show()

##  -----------------------------------------------------------------

def bordas_baseline( img ):
    ''' (BGR) -> binária
    recebe uma imagem BGR e retorna uma imagem binária contendo as bordas, em fundo preto.
    '''
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur  = cv2.GaussianBlur(gray, (5, 5), 0)
    edge = cv2.Canny(blur, 60, 120)
    return edge

##  -----------------------------------------------------------------

def avaliacao( fname, path, bordas=bordas_baseline ):
    '''
    (str, str, function) -> float, dict
    Recebe o nome fname de um arquivo contendo os nomes das imagens a serem avaliadas.
    Path define o caminho onde essas imagens estão salvas no seu computador. 
    bordas é o nome da função que extrai bordas da imagem a ser avaliada.
    Essa função devolve o F-score medio obtido pela função e um dicionário 
    contendo o F-score para cada imagem. 

    PRE-REQUISITOS: essa função depende das seguintes funções que você
    deve obter do seu EP07
        - prec_rec(): 
        - crie_gabarito():

    '''
    scores = {}
    total = 0
    with open(fname, 'r') as arq:
        for linha in arq:
            lin = linha.strip()
            if len(lin) == 0 or lin[0] == '#':
                continue

            campos = lin.split()
            nome = path+campos[0]

            print("Criando o gabarito para ", nome)
            lgabs = []
            for i in [1,2,3]:
                fname = f'{nome} ({i}).jpg'
                baux = cv2.imread( fname )
                lgabs.append( cv2.cvtColor( baux , cv2.COLOR_BGR2GRAY) )
                cv2.imshow(nome, lgabs[i-1])
            gab = crie_gabarito(lgabs)

            if DEBUG:
                cv2.imshow("GABARITO", gab*50)
                cv2.waitKey()

            print("Avaliando a imagem", nome)
            img = cv2.imread( nome+'.jpg' )
            if DEBUG:
                cv2.imshow("Teste", img)
                cv2.waitKey()

            edges = bordas( img )
            p, r = prec_rec(edges, gab)
            fs = 2*r*p/(r+p)
            scores[campos[1]] = fs
            total += fs

    n = len(scores)
    return total/n, scores
