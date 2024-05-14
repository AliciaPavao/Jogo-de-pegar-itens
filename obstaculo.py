import pygame
import random

class Obstaculo:  
    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.posiçãoX = x_inicial
        self.posiçãoY = y_inicial

        self.mascara = pygame.mask.from_surface(self.imagem)

        self.velocidade = random.randint(1,10)

    def movimenta(self):
        self.posiçãoX = self.posiçãoX - self.velocidade
        if self.posiçãoX < -200:
            self.posiçãoX = 850
         


    def desenhar(self, tela):
        tela.blit(self.imagem,(self.posiçãoX, self.posiçãoY))