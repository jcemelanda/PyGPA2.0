from cmath import polar
from math import cos, sin, log10, log
from random import random, randrange
import math
class Gerador:
    @staticmethod
    def constante(n, altura, largura, angulo, constante):
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
        supermat = []
        
        for k in xrange(n):
            mat = []
            for i in xrange(altura):
                line = []
                for j in xrange(largura):
                    zi = complex(i - altura / 2, j - largura / 2) 
                    z = zi - inicio
                    if z == 0 + 0j:
                        f_z = z
                    else:
                        f_z = magnitude / (2 * math.pi * z)
                        f_z = complex(f_z.real, -1 * f_z.imag)
            
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
        supermat = []
        for k in xrange(n):
            mat = []
            for i in xrange(altura):
                line = []
                for j in xrange(largura):
                    zi = complex(i - altura / 2, j - largura / 2) 
                    z = zi - inicio
                    if z == 0 + 0j:
                        f_z = z
                    else:
                        f_z = magnitude / (2 * math.pi * z * z)
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
        supermat = []
        for k in xrange(n):
            mat = []
            for i in xrange(altura):
                line = []
                for j in xrange(largura):
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
        return [[[(x, y) for (x, y) in 
                  zip(
                      [randrange(-1e3, 1e3) / 1000.0 for a in xrange(largura)],
                      [randrange(-1e3, 1e3) / 1000.0 for b in xrange(largura)]
                      )] 
                 for j in xrange(largura)] 
                 for k in xrange(n)] 
             
def test():
    #print Gerador.constante(1, 3, 3, math.pi, 1)
    print Gerador.aleatorio(3, 3, 3)
    #print Gerador.sumidouro(1, 3, 3, 1, 0+0j)
    #print Gerador.turbilhao(1, 3, 3, 1, 1+0j, 0+0j)
    #print Gerador.doublet(1, 3, 3, 1, 0+0j)
                
if __name__ == '__main__':
    test()
