import pygame
import random

class Obstaculo:  
    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.posiçãoX = random.randint(50, 940)
        self.posiçãoY = y_inicial

        self.mascara = pygame.mask.from_surface(self.imagem)

        self.velocidade = random.randint(1,7)

    def movimenta(self):
        self.posiçãoY = self.posiçãoY + self.velocidade
        if self.posiçãoY > 1050:
            self.posiçãoY = -750
            self.posiçãoX = random.randint(50, 940)
         


    def desenhar(self, tela):
        tela.blit(self.imagem,( self.posiçãoX,  self.posiçãoY))