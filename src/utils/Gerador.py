# -*- coding:utf-8 -*-
'''
Módulo que contém a classe geradora de matrizes
'''
#==================================Imports=====================================#

from cmath import polar
from math import cos, sin
from random import randrange
import math


class Gerador:
    '''
    Classe para gerar as matrizes dos campos de gradientes
    '''
    @staticmethod
    def constante(n, altura, largura, angulo, constante):
        '''
        Gera as matrizes de um campo constante
        params:
            n -> int
                Número de Matrizes
            altura -> int
                Altura de cada matriz
            largura -> int
                Largura de cada matriz
            angulo -> int
                Angulo dos vetores
            constante -> int
                Constante para a norma dos vetores
        return:
            list
                Lista de matrizes
        '''
        mat = []
        for i in range(altura):
            line = []
            for j in range(largura):
                x = constante * cos(angulo)
                y = constante * sin(angulo)
                line.append((x, y))
            mat.append(line)
        if n > 1:
            return [mat] * n
        else:
            return [mat]
    
    @staticmethod
    def sumidouro(n, altura, largura, magnitude, inicio, vx=1, vy=1):
        '''
        Gera as matrizes de um campo fonte/sumidouro
        params:
            n -> int
                Número de Matrizes
            altura -> int
                Altura de cada matriz
            largura -> int
                Largura de cada matriz
            magnitude -> int
                Magnitude do campo
            inicio -> int
                Ponto de inicio da movimentação da fonte
            vx -> int
            vy -> int
        return:
            list
                Lista de matrizes
        '''
        supermat = []
        magnitude = complex(magnitude, magnitude)
        
        for k in range(n):
            mat = []
            for i in range(altura):
                line = []
                for j in range(largura):
                    zi = complex(i - altura / 2, j - largura / 2) 
                    z = zi - inicio
                    if z == 0 + 0j:
                        f_z = z
                    else:
                        f_z = magnitude * complex(1, 1) / (2 * math.pi * z)
            
                    modulo, argumento = polar(f_z)
                    x = modulo * cos(argumento)
                    y = modulo * sin(argumento)
                    line.append((x, y))
                mat.append(line)
            supermat.append(mat)
            inicio += complex(vx, vy)
        return supermat
            
    @staticmethod
    def doublet(n, altura, largura, magnitude, inicio, vx=1, vy=1):
        '''
        Gera as matrizes de um campo doublet
        params:
            n -> int
                Número de Matrizes
            altura -> int
                Altura de cada matriz
            largura -> int
                Largura de cada matriz
            magnitude -> int
                Magnitude do campo
            inicio -> int
                Ponto de inicio da movimentação da fonte
            vx -> int
            vy -> int
        return:
            list
                Lista de matrizes
        '''
        if(magnitude.__class__ != complex):
            magnitude = complex(magnitude, magnitude)
        supermat = []
        for k in range(n):
            mat = []
            for i in range(altura):
                line = []
                for j in range(largura):
                    zi = complex(i - altura / 2, j - largura / 2) 
                    z = zi - inicio
                    if z == 0 + 0j:
                        f_z = z
                    else:
                        f_z = magnitude / (2 * math.pi * pow(z, 2))
                    modulo, argumento = polar(f_z)
                    x = modulo * cos(argumento)
                    y = modulo * sin(argumento)
                    line.append((x, y))
                mat.append(line)
            supermat.append(mat)
            inicio += complex(vx, vy)
        return supermat
        
    @staticmethod
    def turbilhao(n, altura, largura, magnitude, posicao, inicio, vx=1, vy=1):
        '''
        Gera as matrizes de um campo turbilhão
        params:
            n -> int
                Número de Matrizes
            altura -> int
                Altura de cada matriz
            largura -> int
                Largura de cada matriz
            magnitude -> int
                Magnitude do campo
            magnitude -> int
                Posição
            inicio -> int
                Ponto de inicio da movimentação da fonte
            vx -> int
            vy -> int
        return:
            list
                Lista de matrizes
        '''
        supermat = []
        for k in range(n):
            mat = []
            for i in range(altura):
                line = []
                for j in range(largura):
                    zi = complex(i - altura / 2, j - largura / 2)
                    z = zi - inicio
                    if(z == 0 + 0j):
                        f_z = z
                    else:
                        f_z = magnitude * posicao / (2 * math.pi * z)
                    modulo, argumento = polar(f_z)
                    x = modulo * cos(argumento)
                    y = modulo * sin(argumento)
                    line.append((x, y))
                mat.append(line)
            supermat.append(mat)
            inicio += complex(vx, vy)
        return supermat
            
    @staticmethod
    def aleatorio(n, altura, largura):
        '''
        Gera as matrizes de um campo turbilhão
        params:
            n -> int
                Número de Matrizes
            altura -> int
                Altura de cada matriz
            largura -> int
                Largura de cada matriz
        return:
            list
                Lista de matrizes
        '''
        return [[[(x, y) for (x, y) in 
                  zip(
                      [randrange(-1e3, 1e3) / 1000.0 for a in range(largura)],
                      [randrange(-1e3, 1e3) / 1000.0 for b in range(largura)]
                      )] 
                 for j in range(largura)] 
                 for k in range(n)] 
             
def test():
    # print(Gerador.constante(1, 3, 3, math.pi, 1))
    # print(Gerador.aleatorio(3, 3, 3))
    print(Gerador.sumidouro(1, 3, 3, 1, 0 + 0j))
    # print(Gerador.turbilhao(1, 3, 3, 1, 1+0j, 0+0j))
    # print(Gerador.doublet(1, 3, 3, 1, 0+0j))
                
if __name__ == '__main__':
    test()
