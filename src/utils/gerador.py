# -*- coding:utf-8 -*-
'''
Módulo que contém a classe geradora de matrizes usando NumPy (Vectorized)
'''
#==================================Imports=====================================#

import numpy as np

class Gerador:
    '''
    Classe para gerar as matrizes dos campos de gradientes usando NumPy
    '''

    @staticmethod
    def _gerar_grade(altura, largura):
        '''
        Gera o grid de coordenadas complexas z
        Centralizado em (altura/2, largura/2)
        '''
        # i (linhas) vai de 0 a altura-1
        # j (colunas) vai de 0 a largura-1
        i = np.arange(altura)
        j = np.arange(largura)
        
        # I, J = np.meshgrid(i, j, indexing='ij')
        
        # I (linhas) -> Coordenada Y (vertical)
        # J (colunas) -> Coordenada X (horizontal)
        
        I, J = np.meshgrid(i, j, indexing='ij')
        
        # Centraliza a grade
        # Z = X + iY
        # Nota: Em imagens, Y cresce para baixo.
        # Isso é consistente com as coordenadas de tela.
        Z = (J - largura / 2) + 1j * (I - altura / 2)
        return Z
    
    @staticmethod
    def constante(n, altura, largura, angulo, constante):
        '''
        Gera campo constante (Vetorizado)
        '''
        # Calculado apenas uma vez
        val_x = constante * np.cos(angulo)
        val_y = constante * np.sin(angulo)
        # val = Real(X) + j*Imag(Y)
        # Consistente com a nova Grade: Real é X (horizontal), Imag é Y (vertical)
        val = val_x + 1j * val_y 
        
        # Formato de retorno: (n, altura, largura) complex128
        mat = np.full((altura, largura), val_x + 1j * val_y, dtype=np.complex128)
        
        # Transmite (broadcast) para n quadros
        if n > 0:
            return np.tile(mat, (n, 1, 1))
        return mat[np.newaxis, ...] # (1, h, w)
    
    @staticmethod
    def sumidouro(n, altura, largura, magnitude, inicio, vx=0, vy=0):
        '''
        Gera campo Sumidouro (Vetorizado)
        V = m / (2*pi*conj(z))
        '''
        if isinstance(magnitude, complex):
            magnitude = magnitude.real
            
        # Cria a grade base
        Z = Gerador._gerar_grade(altura, largura) # (h, w)
        
        # Passos de tempo k=0..n-1
        k = np.arange(n)
        
        # Vetor de movimento ao longo do tempo
        # Pos no tempo k = inicio + k*(vx + 1j*vy)
        velocidade = vx + 1j * vy
        centros = inicio + np.outer(k, velocidade) 
        # centros precisa ser (n, 1, 1) para broadcast com (h, w)
        centros = centros.reshape(n, 1, 1)
        
        # Transmite Z para (n, h, w)
        Z_t = Z[np.newaxis, ...] - centros
        
        # Evita divisão por zero
        # Cria mascara onde Z_t é aproximadamente 0
        mascara_singularidade = np.abs(Z_t) < 1e-9
        Z_t[mascara_singularidade] = 1e-9 # Previne NaN
        
        F_z = magnitude / (2 * np.pi * np.conj(Z_t))
        F_z[mascara_singularidade] = 0 # Singularidade é 0
        
        return F_z
            
    @staticmethod
    def doublet(n, altura, largura, magnitude, inicio, vx=0, vy=0):
        '''
        Gera campo Doublet (Vetorizado)
        V = -m / (2*pi*conj(z)^2)
        '''
        if isinstance(magnitude, complex):
             magnitude = magnitude.real
             
        Z = Gerador._gerar_grade(altura, largura)
        k = np.arange(n)
        velocidade = vx + 1j * vy
        centros = (inicio + np.outer(k, velocidade)).reshape(n, 1, 1)
        
        Z_t = Z[np.newaxis, ...] - centros
        
        mascara_singularidade = np.abs(Z_t) < 1e-9
        Z_t[mascara_singularidade] = 1e-9
        
        F_z = -magnitude / (2 * np.pi * (np.conj(Z_t)**2))
        F_z[mascara_singularidade] = 0
        
        return F_z
        
    @staticmethod
    def turbilhao(n, altura, largura, magnitude, posicao, inicio, vx=0, vy=0):
        '''
        Gera campo Turbilhao (Vetorizado)
        V = -i * m / (2*pi*conj(z))
        '''
        if isinstance(magnitude, complex):
            magnitude = magnitude.real

        Z = Gerador._gerar_grade(altura, largura)
        k = np.arange(n)
        velocidade = vx + 1j * vy
        centros = (inicio + np.outer(k, velocidade)).reshape(n, 1, 1)
        
        Z_t = Z[np.newaxis, ...] - centros
        
        mascara_singularidade = np.abs(Z_t) < 1e-9
        Z_t[mascara_singularidade] = 1e-9
        
        # -1j * magnitude / ...
        F_z = -1j * magnitude / (2 * np.pi * np.conj(Z_t))
        F_z[mascara_singularidade] = 0
        
        return F_z
            
    @staticmethod
    def aleatorio(n, altura, largura):
        '''
        Gera campo aleatorio (Vetorizado)
        '''
        # Partes real e imaginária aleatórias entre -1 e 1
        parte_real = np.random.uniform(-1, 1, (n, altura, largura))
        parte_imag = np.random.uniform(-1, 1, (n, altura, largura))
        return parte_real + 1j * parte_imag
             
def test():
    import time
    start = time.time()
    m = Gerador.sumidouro(50, 100, 100, 1, 0, 1, 1)
    end = time.time()
    print(f"Generated shape {m.shape} in {end-start:.4f}s")
    print(f"Sample: {m[0, 50, 50]}")

if __name__ == '__main__':
    test()
