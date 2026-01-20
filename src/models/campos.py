# -*- coding: utf-8 -*-
'''
Módulo que contém as classes de modelos dos campos de gradientes.
'''

class CampoAleatorio:
    '''
    Classe que representa um campo aleatório
    '''
    type = 0  # Atributo que define o tipo do campo
    
    def __init__(self, n=0, h=1, w=1, mat=None):
        '''
        Inicializa os atributos do campo aleatório
        params:
            n -> int
                Número de matrizes
            h -> int
                Altura das matrizes
            w -> int
                Largura das matrizes
            mat -> list
                Lista de Matrizes
        '''
        self.num_mat = n
        self.altura = h
        self.largura = w
        self.mat = mat if mat is not None else []
        
    def __str__(self):
        '''
        Gera uma versão textual do campo aleatório
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Aleatório'+\
                '\nn: '+str(self.num_mat)+\
                '\naltura: '+str(self.altura)+\
                '\nlargura: '+str(self.largura)+\
                '\ncampos: '
        for c in self.mat:
            texto += str_mat(c)+'\n'
        return texto


class CampoCombinado:
    '''
    Classe que representa um campo gerado pela combinação de dois ou mais campos
    '''
    type = 5
    
    def __init__(self, n=0, h=1, w=1, mat=None, campos=None):
        '''
        Inicializa os atributos do campo combinado
        params:
            n -> int
                Número de matrizes
            h -> int
                Altura das matrizes
            w -> int
                Largura das matrizes
            mat -> list
                Lista de Matrizes
            campos -> list
                Lista dos campos que foram combinados
        '''
        self.num_mat = n
        self.altura = h
        self.largura = w
        self.mat = mat if mat is not None else []
        self.campos = campos if campos is not None else []
    
    def __str__(self):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Combinado'+\
                '\nn: '+str(self.num_mat)+\
                '\naltura: '+str(self.altura)+\
                '\nlargura: '+str(self.largura)+\
                '\ncampos: \n'
        for c in self.mat:
            texto += str_mat(c)+'\n'
        texto += '\ncomponentes: \n'+self.mostra_campos()
        return texto
    
    def mostra_campos(self):
        '''
        Gera a versão textual do conjunto de campos combinados
        return:
            string
                Versão textual dos campos
        '''
        t = ''
        for campo in self.campos[:]:
            t += str(campo)+'\n'
        return t


class CampoConstante:
    '''
    Classe que representa um campo onde todos os vetores são iguais
    '''
    type = 1
    
    def __init__(self, n=0, h=1, w=1, c=0, a=0, mat=None):
        '''
        Inicializa os atributos do campo constante
        params:
            n -> int
                Número de matrizes
            h -> int
                Altura das matrizes
            w -> int
                Largura das matrizes
            c -> int
                Constante para cálculo da norma dos vetores
            a -> int
                Ângulo dos vetores
            mat -> list
                Lista de Matrizes
        '''
        self.num_mat = n
        self.altura = h
        self.largura = w
        self.constante = c
        self.angulo = a
        self.mat = mat if mat is not None else []
    
    def __str__(self):
        '''
        Gera uma versão textual do campo constante
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Constante'+\
                '\nn: '+str(self.num_mat)+\
                '\naltura: '+str(self.altura)+\
                '\nlargura: '+str(self.largura)+\
                '\nconstante: '+str(self.constante)+\
                '\nangulo: '+str(self.angulo)+\
                '\ncampos: \n'
        for c in self.mat:
            texto += str_mat(c)+'\n'
        return texto
    
    @property
    def const_1(self):
        '''
        Getter para a constante 1 (constante)
        return:
            int
                A constante de geração do campo
        '''
        return self.constante
    
    @property
    def const_2(self):
        '''
        Getter para a constante 2 (ângulo)
        return:
            int
                Ângulo dos vetores
        '''
        return self.angulo


class CampoDoublet:
    '''
    Classe que representa um campo doublet
    '''
    type = 2
    
    def __init__(self, n=0, h=1, w=1, p=0, m=0, mat=None):
        '''
        Inicializa os atributos do campo doublet
        params:
            n -> int
                Número de matrizes
            h -> int
                Altura das matrizes
            w -> int
                Largura das matrizes
            p -> int
                Início
            m -> int
                Magnitude do campo
            mat -> list
                Lista de Matrizes
        '''
        self.num_mat = n
        self.altura = h
        self.largura = w
        self.inicio = p
        self.magnitude = m
        self.mat = mat if mat is not None else []
    
    def __str__(self):
        '''
        Gera uma versão textual do campo doublet
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Doublet'+\
                '\nn: '+str(self.num_mat)+\
                '\naltura: '+str(self.altura)+\
                '\nlargura: '+str(self.largura)+\
                '\ninicio: '+str(self.inicio)+\
                '\nmagnitude: '+str(self.magnitude)+\
                '\ncampos: \n'
        for c in self.mat:
            texto += str_mat(c)+'\n'
        return texto
    
    @property
    def const_1(self):
        '''
        Getter para a constante 1 (magnitude)
        return:
            int
                A constante de geração do campo
        '''
        return self.magnitude


class CampoFonte:
    '''
    Classe que representa um campo fonte / sumidouro
    '''
    type = 3
    
    def __init__(self, n=0, h=1, w=1, p=0, m=0, mat=None):
        '''
        Inicializa os atributos do campo fonte
        params:
            n -> int
                Número de matrizes
            h -> int
                Altura das matrizes
            w -> int
                Largura das matrizes
            p -> int
                Início
            m -> int
                Magnitude do campo
            mat -> list
                Lista de Matrizes
        '''
        self.num_mat = n
        self.altura = h
        self.largura = w
        self.inicio = p
        self.magnitude = m
        self.mat = mat if mat is not None else []
    
    def __str__(self):
        '''
        Gera uma versão textual do campo fonte
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Fonte'+\
                '\nn: '+str(self.num_mat)+\
                '\naltura: '+str(self.altura)+\
                '\nlargura: '+str(self.largura)+\
                '\ninicio: '+str(self.inicio)+\
                '\nmagnitude: '+str(self.magnitude)+\
                '\ncampos: \n'
        for c in self.mat:
            texto += str_mat(c)+'\n'
        return texto
    
    @property
    def const_1(self):
        '''
        Getter para a constante 1 (magnitude)
        return:
            int
                A constante de geração do campo
        '''
        return self.magnitude


class CampoTurbilhao:
    '''
    Classe que representa um campo turbilhão
    '''
    type = 4
    
    def __init__(self, n=0, h=1, w=1, p=0, m=0, ic=0, mat=None):
        '''
        Inicializa os atributos do campo turbilhão
        params:
            n -> int
                Número de matrizes
            h -> int
                Altura das matrizes
            w -> int
                Largura das matrizes
            p -> int
                Início
            m -> int
                Magnitude do campo
            ic -> complex
                Posição Complexa
            mat -> list
                Lista de Matrizes
        '''
        self.num_mat = n
        self.altura = h
        self.largura = w
        self.inicio = p
        self.magnitude = m
        self.posicao = ic
        self.mat = mat if mat is not None else []
    
    def __str__(self):
        '''
        Gera uma versão textual do campo turbilhão
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Turbilhão'+\
                '\nn: '+str(self.num_mat)+\
                '\naltura: '+str(self.altura)+\
                '\nlargura: '+str(self.largura)+\
                '\ninicio: '+str(self.inicio)+\
                '\nmagnitude: '+str(self.magnitude)+\
                '\nposicao: '+str(self.posicao)+\
                '\ncampos: \n'
        for c in self.mat:
            texto += str_mat(c)+'\n'
        return texto
    
    @property
    def const_1(self):
        '''
        Getter para a constante 1 (magnitude)
        return:
            int
                A constante de geração do campo
        '''
        return self.magnitude
    
    @property
    def const_2(self):
        '''
        Getter para a constante 2 (posição)
        return:
            complex
                Posição complexa
        '''
        return self.posicao


def str_mat(mat):
    '''
    Cria uma versão textual de uma matriz bidimensional
    '''
    t = '[\n'
    for i in range(len(mat)):
        t += '[ '
        for j in range(len(mat[0])):
            t += str(mat[i][j])+' '
        t+=']\\n'
    t += ']'
    return t
    

if __name__ == '__main__':
    a = CampoAleatorio()
    a.mat = [[[1, 2], [2, 3]],[[2, 1], [4, 3]]]
