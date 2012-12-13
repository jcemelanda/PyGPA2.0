# -*- coding: utf-8 -*-
class campo_aleatorio:
    __type__ = 0
    def __init__(self, n=0, h=1, w=1, mat=[]):
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._mat = mat
        
    def __str__(self):
        texto = 'Campo Aleatório'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ncampos: '
        for c in self._mat:
            texto += str_mat(c)+'\n'
        return texto
        
    def set_num_mat(self, n):
        self._num_mat = n
    
    def set_altura(self, h):
        self._altura = h
        
    def set_largura(self, w):
        self._largura = w
        
    def set_mat(self, mat):
        self._mat = mat
        
    def get_num_mat(self):
        return self._num_mat
    
    def get_altura(self):
        return self._altura
    
    def get_largura(self):
        return self._largura

    def get_mat(self):
        return self._mat
    
    def get_type(self):
        return self.__type__

class campo_combinado:
    __type__ = 5
    def __init__(self, n=0, h=1, w=1, mat=[], campos=[]):
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._mat = mat
        self._campos = campos
        
    def __str__(self):
        texto = 'Campo Combinado'+\
                '\nn: '+str(self._num_mat)+\
                '\naltura: '+str(self._altura)+\
                '\nlargura: '+str(self._largura)+\
                '\ncampos: \n'
        for c in self._mat:
            texto += str_mat(c)+'\n'
        texto += '\ncomponentes: \n'+self.mostra_campos()
        return texto
        
    def set_num_mat(self, n):
        self._num_mat = n
    
    def set_altura(self, h):
        self._altura = h
        
    def set_largura(self, w):
        self._largura = w
        
    def set_mat(self, mat):
        self._mat = mat
        
    def set_campos(self, campos):
        self._campos = campos
        
    def get_num_mat(self):
        return self._num_mat
    
    def get_altura(self):
        return self._altura
    
    def get_largura(self):
        return self._largura

    def get_mat(self):
        return self._mat
    
    def get_campo(self):
        return self._campos
    
    def get_type(self):
        return self.__type__
    
    def mostra_campos(self):
        t = ''
        for campo in self._campos[:]:
            t += str(campo)+'\n'
        return t
        
class campo_constante:
    __type__ = 1
    def __init__(self, n=0, h=1, w=1, c=0, a=0, mat=[]):
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._constante = c
        self._angulo = a
        self._mat = mat
        
    def __str__(self):
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
    def set_num_mat(self, n):
        self._num_mat = n
    
    def set_altura(self, h):
        self._altura = h
        
    def set_largura(self, w):
        self._largura = w
        
    def set_cosntante(self, c):
        self._constante = c
    
    def set_angulo(self, a):
        self._angulo = a
        
    def set_mat(self, mat):
        self._mat = mat
        
    def get_num_mat(self):
        return self._num_mat
    
    def get_altura(self):
        return self._altura
    
    def get_largura(self):
        return self._largura
    
    def get_constante(self):
        return self._constante
    
    def get_angulo(self):
        return self._angulo
    
    def get_const_1(self):
        return self._constante
    
    def get_const_2(self):
        return self._angulo

    def get_mat(self):
        return self._mat
    def get_type(self):
        return self.__type__
    
class campo_doublet:
    __type__ = 2
    def __init__(self, n=0, h=1, w=1, p=0, m=0, mat=[]):
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._inicio = p
        self._magnitude = m
        self._mat = mat
        
    def __str__(self):
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
    
    def set_num_mat(self, n):
        self._num_mat = n
    
    def set_altura(self, h):
        self._altura = h
        
    def set_largura(self, w):
        self._largura = w
        
    def set_inicio(self, p):
        self._inicio = p
    
    def set_magnitude(self, m):
        self._magnitude = m
        
    def set_mat(self, mat):
        self._mat = mat
        
    def get_num_mat(self):
        return self._num_mat
    
    def get_altura(self):
        return self._altura
    
    def get_largura(self):
        return self._largura
    
    def get_inicio(self):
        return self._inicio
    
    def get_magnitude(self):
        return self._magnitude

    def get_const_1(self):
        return self._magnitude
    
    def get_mat(self):
        return self._mat
    
    def get_type(self):
        return self.__type__
    
class campo_fonte:
    __type__ = 3
    def __init__(self, n=0, h=1, w=1, p=0, m=0, mat=[]):
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._inicio = p
        self._magnitude = m
        self._mat = mat
        
    def __str__(self):
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
        self._num_mat = n
    
    def set_altura(self, h):
        self._altura = h
        
    def set_largura(self, w):
        self._largura = w
        
    def set_inicio(self, p):
        self._inicio = p
    
    def set_magnitude(self, m):
        self._magnitude = m
        
    def set_mat(self, mat):
        self._mat = mat
        
    def get_num_mat(self):
        return self._num_mat
    
    def get_altura(self):
        return self._altura
    
    def get_largura(self):
        return self._largura
    
    def get_inicio(self):
        return self._inicio
    
    def get_magnitude(self):
        return self._magnitude

    def get_const_1(self):
        return self._magnitude
    
    def get_mat(self):
        return self._mat
    
    def get_type(self):
        return self.__type__
    
class campo_turbilhao:
    __type__ = 4
    def __init__(self, n=0, h=1, w=1, p=0, m=0, ic=0, mat=[]):
        self._num_mat = n
        self._altura = h
        self._largura = w
        self._inicio = p
        self._magnitude = m
        self._posicao = ic
        self._mat = mat
    
    def __str__(self):
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
        self._num_mat = n
    
    def set_altura(self, h):
        self._altura = h
        
    def set_largura(self, w):
        self._largura = w
        
    def set_inicio(self, p):
        self._inicio = p
    
    def set_magnitude(self, m):
        self._magnitude = m
        
    def set_posicao(self, ic):
        self._posicao = ic
        
    def set_mat(self, mat):
        self._mat = mat
        
    def get_num_mat(self):
        return self._num_mat
    
    def get_altura(self):
        return self._altura
    
    def get_largura(self):
        return self._largura
    
    def get_inicio(self):
        return self._inicio
    
    def get_magnitude(self):
        return self._magnitude

    def get_posicao(self):
        return self._posicao
    
    def get_const_1(self):
        return self._magnitude
    
    def get_const_2(self):
        return self._posicao
    
    def get_mat(self):
        return self._mat
    
    def get_type(self):
        return self.__type__
    
def str_mat(mat):
    t = '[\n'
    for i in xrange(len(mat)):
        t += '[ '
        for j in xrange(len(mat[0])):
            t += str(mat[i][j])+' '
        t+=']\n'
    t += ']'
    return t
    
if __name__ == '__main__':
    a = campo_aleatorio()
    a.set_mat([[[1, 2], [2, 3]],[[2, 1], [4, 3]]])
    print(a)