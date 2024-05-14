import pygame

class Personagem:

    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.posiçãoX = x_inicial
        self.posiçãoY = y_inicial

        self.mascara = pygame.mask.from_surface(self.imagem)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.posiçãoX, self.posiçãoY))

    def andar(self):
    # Desenhando as imagens
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            if self.posiçãoX < 840:
                self.posiçãoX = self.posiçãoX + 5
    
        if teclas[pygame.K_LEFT]:
            if self.posiçãoX > 0:
                self.posiçãoX = self.posiçãoX - 5

        if teclas[pygame.K_UP]:
            if self.posiçãoY > 0:
                self.posiçãoY = self.posiçãoY - 5

        if teclas[pygame.K_DOWN]:
            if self.posiçãoY < 550:
                self.posiçãoY = self.posiçãoY + 5