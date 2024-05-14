import pygame
from personagens import Personagem

pygame.init()
#Construindo a tela
tela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Jogo do chinbinho")
tela.fill((117, 75, 19))


# Carregando imagens
fundo = Personagem("imagem/fundo.png", 1000, 700, 0, 0 )

# Criando um relógio para configurar o fps
clock = pygame.time.Clock()

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
     

    fundo.desenhar(tela)

    # Atualizando a tela
    pygame.display.update()

    # Regulando o FPS 
    clock.tick(60)