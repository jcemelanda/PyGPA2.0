# -*- coding: utf-8 -*-
'''
Módulo que contém as clásses de modelos dos campos de gradientes.
'''
class campo_aleatorio:
    '''
    Classe que representa um campos aleatório
    '''
    #Atributo que define o tipo do campo
    __type__ = 0
    def __init__(self, n=0, h=1, w=1, mat=[]):
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
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._mat = mat
        
    def __str__(self):
        '''
        Gera uma versão textual do campo aleatório
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Aleatório'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ncampos: '
        for c in self._mat:
            texto += str_mat(c)+'\n'
        return texto
        
#=====================================setters==================================#
    
    def set_num_mat(self, n):
        '''
        Setter para o número de matrizes
        params:
            n -> int
                Número de matrizes do campos
        '''
        self._num_mat = n
    
    def set_altura(self, h):
        '''
        Setter para a altura das matrizes
        params:
            h -> int
                Altura das matrizes do campos
        '''
        self._altura = h
    
    def set_largura(self, w):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._largura = w
    
    def set_mat(self, mat):
        '''
        Setter para as matrizes
        params:
            mat -> list
                matrizes do campos
        '''
        self._mat = mat
    
#======================================getters=================================#
    
    def get_num_mat(self):
        '''
        Getter para o número de matrizes
        return:
            int
                número de matrizes do campo
        '''
        return self._num_mat
    
    def get_altura(self):
        '''
        Getter para a altura das matrizes
        return:
            int
                altura das matrizes do campo
        '''
        return self._altura
    
    def get_largura(self):
        '''
        Getter para a largura das matrizes
        return:
            int
                largura das matrizes do campo
        '''
        return self._largura
    
    def get_mat(self):
        '''
        Getter para as matrizes
        return:
            list
                matrizes do campo
        '''
        return self._mat
    
    def get_type(self):
        '''
        Getter para o tipo do campo
        return:
            int
                Tipo do campo
        '''
        return self.__type__
    
class campo_combinado:
    '''
    Classe que representa um campo gerado pela combinação de dois ou mais campos
    '''
    __type__ = 5
    def __init__(self, n=0, h=1, w=1, mat=[], campos=[]):
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
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._mat = mat
        self._campos = campos
    
    def __str__(self):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Combinado'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ncampos: \n'
        for c in self._mat:
            texto += str_mat(c)+'\n'
        texto += '\ncomponentes: \n'+self.mostra_campos()
        return texto

#=====================================setters==================================#

    def set_num_mat(self, n):
        '''
        Setter para o número de matrizes
        params:
            n -> int
                Número de matrizes do campos
        '''
        self._num_mat = n
    
    def set_altura(self, h):
        '''
        Setter para a altura das matrizes
        params:
            h -> int
                Altura das matrizes do campos
        '''
        self._altura = h
    
    def set_largura(self, w):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._largura = w
    
    def set_mat(self, mat):
        '''
        Setter para as matrizes
        params:
            mat -> list
                Matrizes do campo
        '''
        self._mat = mat
    
    def set_campos(self, campos):
        '''
        Setter para os campos que formam o campo
        params:
            campo -> campo_aleatorio, campo_combinado, campo_constante, 
            campo_doublet, campo_fonte, campo_turbilhao, campo_combinado
                Campos que compõe o campo combinado
        '''
        self._campos = campos
    
#=====================================getters==================================#
    
    def get_num_mat(self):
        '''
        Getter para o número de matrizes
        return:
            int
                número de matrizes do campo
        '''
        return self._num_mat
    
    def get_altura(self):
        '''
        Getter para a altura das matrizes
        return:
            int
                altura das matrizes do campo
        '''
        return self._altura
    
    def get_largura(self):
        '''
        Getter para a largura das matrizes
        return:
            int
                largura das matrizes do campo
        '''
        return self._largura
    
    def get_mat(self):
        '''
        Getter para as matrizes
        return:
            list
                matrizes do campo
        '''
        return self._mat
    
    def get_campos(self):
        '''
        Getter para os campos que compõe o campo
        return:
            list
                campos da combinação
        '''
        return self._campos
    
    def get_type(self):
        '''
        Getter para o tipo do campo
        return:
            int
                Tipo do campo
        '''
        return self.__type__
    
    def mostra_campos(self):
        '''
        Gera a versão textual do conjunto de campos combinados
        return:
            string
                Versão textual dos campos
        '''
        t = ''
        for campo in self._campos[:]:
            t += str(campo)+'\n'
        return t
    
class campo_constante:
    '''
    Classe que representa um campo onde todos os vetores são iguais
    '''
    __type__ = 1
    def __init__(self, n=0, h=1, w=1, c=0, a=0, mat=[]):
        '''
        Inicializa os atributos do campo aleatório
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
                Angulo dos vetores
            mat -> list
                Lista de Matrizes
        '''
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._constante = c
        self._angulo = a
        self._mat = mat
    
    def __str__(self):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Constante'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\nconstante: '+str(self._constante)+\
                '\nangulo: '+str(self._angulo)+\
                '\ncampos: \n'
        for c in self._mat:
            texto += str_mat(c)+'\n'
        return texto
    
#=====================================setters==================================#
    
    def set_num_mat(self, n):
        '''
        Setter para o número de matrizes
        params:
            n -> int
                Número de matrizes do campos
        '''
        self._num_mat = n
    
    def set_altura(self, h):
        '''
        Setter para a altura das matrizes
        params:
            h -> int
                Altura das matrizes do campos
        '''
        self._altura = h
    
    def set_largura(self, w):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._largura = w
    
    def set_cosntante(self, c):
        '''
        Setter para a constante de geração dos vetores
        params:
            constante -> int
                Constante para gerar os vetores
        '''
        self._constante = c
    
    def set_angulo(self, a):
        '''
        Setter para o angulo dos vetores
        params:
            mat -> list
                Matrizes do campo
        '''
        self._angulo = a
    
    def set_mat(self, mat):
        '''
        Setter para as matrizes
        params:
            mat -> list
                Matrizes do campo
        '''
        self._mat = mat
    
#=====================================getters==================================#
    
    def get_num_mat(self):
        '''
        Getter para o número de matrizes
        return:
            int
                número de matrizes do campo
        '''
        return self._num_mat
    
    def get_altura(self):
        '''
        Getter para a altura das matrizes
        return:
            int
                altura das matrizes do campo
        '''
        return self._altura
    
    def get_largura(self):
        '''
        Getter para a largura das matrizes
        return:
            int
                largura das matrizes do campo
        '''
        return self._largura
    
    def get_constante(self):
        '''
        Getter para a constante geradora dos vetores
        return:
            int
                constante geradora dos vetores
        '''
        return self._constante
    
    def get_angulo(self):
        '''
        Getter para o angulo dos vetores
        return:
            int
                Angulo dos vetores
        '''
        return self._angulo
    
    def get_const_1(self):
        '''
        Getter para a constante 1 (cosntante)
        return:
            int
                A constante de geração do campo
        '''
        return self.get_constante()
    
    def get_const_2(self):
        '''
        Getter para a constante 2 (angulo)
        return:
            int
                Angulo dos vetores
        '''
        return self.get_angulo()
    
    def get_mat(self):
        '''
        Getter para as matrizes
        return:
            list
                matrizes do campo
        '''
        return self._mat
    
    def get_type(self):
        '''
        Getter para o tipo do campo
        return:
            int
                Tipo do campo
        '''
        return self.__type__
    
class campo_doublet:
    '''
    Classe que representa um campo doublet
    '''
    __type__ = 2
    def __init__(self, n=0, h=1, w=1, p=0, m=0, mat=[]):
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
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._inicio = p
        self._magnitude = m
        self._mat = mat
    
    def __str__(self):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Doublet'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ninicio: '+str(self._inicio)+\
                '\nmagnitude: '+str(self._magnitude)+\
                '\ncampos: \n'
        for c in self._mat:
            texto += str_mat(c)+'\n'
        return texto
    
#=====================================setters==================================#
    
    def set_num_mat(self, n):
        '''
        Setter para o número de matrizes
        params:
            n -> int
                Número de matrizes do campos
        '''
        self._num_mat = n
    
    def set_altura(self, h):
        '''
        Setter para a altura das matrizes
        params:
            h -> int
                Altura das matrizes do campos
        '''
        self._altura = h
    
    def set_largura(self, w):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._largura = w
    
    def set_inicio(self, p):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._inicio = p
    
    def set_magnitude(self, m):
        '''
        Setter para a magnitude dos vetores
        params:
            m -> int
                Magnitude dos vetores
        '''
        self._magnitude = m
    
    def set_mat(self, mat):
        '''
        Setter para as matrizes
        params:
            mat -> list
                Matrizes do campo
        '''
        self._mat = mat
    
#=====================================getters==================================#
    
    def get_num_mat(self):
        '''
        Getter para o número de matrizes
        return:
            int
                número de matrizes do campo
        '''
        return self._num_mat
    
    def get_altura(self):
        '''
        Getter para a altura das matrizes
        return:
            int
                altura das matrizes do campo
        '''
        return self._altura
    
    def get_largura(self):
        '''
        Getter para a largura das matrizes
        return:
            int
                largura das matrizes do campo
        '''
        return self._largura
    
    def get_inicio(self):
        '''
        Getter para a a magnitude do campo
        return:
            int
                constante geradora dos vetores
        '''
        return self._inicio
    
    def get_magnitude(self):
        '''
        Getter para a a magnitude do campo
        return:
            int
                constante geradora dos vetores
        '''
        return self._magnitude
    
    def get_const_1(self):
        '''
        Getter para a constante 1 (magnitude)
        return:
            int
                A constante de geração do campo
        '''
        return self.get_magnitude()
    
    def get_mat(self):
        '''
        Getter para as matrizes
        return:
            list
                matrizes do campo
        '''
        return self._mat
    
    def get_type(self):
        '''
        Getter para o tipo do campo
        return:
            int
                Tipo do campo
        '''
        return self.__type__
    
class campo_fonte:
    '''
    Classe que representa um campo fonte / sumidouro
    '''
    __type__ = 3
    def __init__(self, n=0, h=1, w=1, p=0, m=0, mat=[]):
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
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._inicio = p
        self._magnitude = m
        self._mat = mat
    
    def __str__(self):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Fonte'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ninicio: '+str(self._inicio)+\
                '\nmagnitude: '+str(self._magnitude)+\
                '\ncampos: \n'
        for c in self._mat:
            texto += str_mat(c)+'\n'
        return texto
    
    def set_num_mat(self, n):
        '''
        Setter para o número de matrizes
        params:
            n -> int
                Número de matrizes do campos
        '''
        self._num_mat = n
    
    def set_altura(self, h):
        '''
        Setter para a altura das matrizes
        params:
            h -> int
                Altura das matrizes do campos
        '''
        self._altura = h
    
    def set_largura(self, w):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._largura = w
    
    def set_inicio(self, p):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._inicio = p
    
    def set_magnitude(self, m):
        '''
        Setter para a magnitude do campo
        params:
            m
                constante geradora dos vetores
        '''
        self._magnitude = m
    
    def set_mat(self, mat):
        '''
        Setter para as matrizes
        params:
            mat -> list
                Matrizes do campo
        '''
        self._mat = mat
    
    def get_num_mat(self):
        '''
        Getter para o número de matrizes
        return:
            int
                número de matrizes do campo
        '''
        return self._num_mat
    
    def get_altura(self):
        '''
        Getter para a altura das matrizes
        return:
            int
                altura das matrizes do campo
        '''
        return self._altura
    
    def get_largura(self):
        '''
        Getter para a largura das matrizes
        return:
            int
                largura das matrizes do campo
        '''
        return self._largura
    
    def get_inicio(self):
        '''
        Getter para a a magnitude do campo
        return:
            int
                constante geradora dos vetores
        '''
        return self._inicio
    
    def get_magnitude(self):
        '''
        Getter para a a magnitude do campo
        return:
            int
                constante geradora dos vetores
        '''
        return self._magnitude
    
    def get_const_1(self):
        '''
        Getter para a constante 1 (magnitude)
        return:
            int
                A constante de geração do campo
        '''
        return self.get_magnitude()
    
    def get_mat(self):
        '''
        Getter para as matrizes
        return:
            list
                matrizes do campo
        '''
        return self._mat
    
    def get_type(self):
        '''
        Getter para o tipo do campo
        return:
            int
                Tipo do campo
        '''
        return self.__type__
    
class campo_turbilhao:
    '''
    Classe que representa um campo turbilhão
    '''
    __type__ = 4
    def __init__(self, n=0, h=1, w=1, p=0, m=0, ic=0, mat=[]):
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
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._inicio = p
        self._magnitude = m
        self._posicao = ic
        self._mat = mat
    
    def __str__(self):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        texto = 'Campo Turbilhão'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ninicio: '+str(self._inicio)+\
                '\nmagnitude: '+str(self._magnitude)+\
                '\nposicao: '+str(self._posicao)+\
                '\ncampos: \n'
        for c in self._mat:
            texto += str_mat(c)+'\n'
        return texto
    
    def set_num_mat(self, n):
        '''
        Gera uma versão textual do campo combinado
        return:
            string
                Versão textual do campo
        '''
        self._num_mat = n
    
    def set_altura(self, h):
        '''
        Setter para a altura das matrizes
        params:
            h -> int
                Altura das matrizes do campos
        '''
        self._altura = h
    
    def set_largura(self, w):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._largura = w
    
    def set_inicio(self, p):
        '''
        Setter para a largura das matrizes
        params:
            w -> int
                Largura das matrizes do campos
        '''
        self._inicio = p
    
    def set_magnitude(self, m):
        '''
        Setter para a magnitude do campo
        params:
            m
                constante geradora dos vetores
        '''
        self._magnitude = m
    
    def set_posicao(self, ic):
        '''
        Setter para a posição
        params:
            m -> complex
                posição
        '''
        self._posicao = ic
    
    def set_mat(self, mat):
        '''
        Setter para as matrizes
        params:
            mat -> list
                Matrizes do campo
        '''
        self._mat = mat
    
    def get_num_mat(self):
        '''
        Getter para o número de matrizes
        return:
            int
                número de matrizes do campo
        '''
        return self._num_mat
    
    def get_altura(self):
        '''
        Getter para a altura das matrizes
        return:
            int
                altura das matrizes do campo
        '''
        return self._altura
    
    def get_largura(self):
        '''
        Getter para a largura das matrizes
        return:
            int
                largura das matrizes do campo
        '''
        return self._largura
    
    def get_inicio(self):
        '''
        Getter para a a magnitude do campo
        return:
            int
                constante geradora dos vetores
        '''
        return self._inicio
    
    def get_magnitude(self):
        '''
        Getter para a a magnitude do campo
        return:
            int
                constante geradora dos vetores
        '''
        return self._magnitude
    
    def get_posicao(self):
        '''
        Getter para aposição
        return:
            complex
                posição
        '''
        return self._posicao
    
    def get_const_1(self):
        '''
        Getter para a constante 1 (magnitude)
        return:
            int
                A constante de geração do campo
        '''
        return self.get_magnitude()
    
    def get_const_2(self):
        '''
        Getter para a constante 2 (posicao)
        return:
            int
                Angulo dos vetores
        '''
        return self.get_posicao()
    
    def get_mat(self):
        '''
        Getter para as matrizes
        return:
            list
                matrizes do campo
        '''
        return self._mat
    
    def get_type(self):
        '''
        Getter para o tipo do campo
        return:
            int
                Tipo do campo
        '''
        return self.__type__
    
def str_mat(mat):
    '''
    Cria uma versão textual de uma matriz bidimensional
    '''
    t = '[\n'
    for i in range(len(mat)):
        t += '[ '
        for j in range(len(mat[0])):
            t += str(mat[i][j])+' '
        t+=']\n'
    t += ']'
    return t
    
if __name__ == '__main__':
    a = campo_aleatorio()
    a.set_mat([[[1, 2], [2, 3]],[[2, 1], [4, 3]]])
