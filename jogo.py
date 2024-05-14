import pygame
from personagens import Personagem
from obstaculo import Obstaculo

pygame.init()
#Construindo a tela
tela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Jogo do chinbinho")
tela.fill((117, 75, 19))

pontuacao = 0

# Carregando imagens
fundo = Personagem("imagem/fundo.png", 1000, 700, 0, 0 )
borboleta = Personagem("imagem/borboleta.png", 190, 180, 80, 10 ) 


# Carregando imagens
# Criando personagens
lista_itens = [ 
Obstaculo("imagem/açucar.png", 50, 60, 80, 10 ),
Obstaculo("imagem/chocolate.png", 50, 60, 350, 450),
Obstaculo("imagem/colher.png", 50, 60, 640,10 ),
Obstaculo("imagem/leite.png", 50, 60, 90, 90 ),
Obstaculo("imagem/manteiga.png", 50, 60, 90, 90 )
]



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

    for obstaculo in lista_itens:
        obstaculo.movimenta()
        obstaculo.desenhar(tela)

    
    borboleta.desenhar(tela)
    borboleta.andar()
    

    # Atualizando a tela
    pygame.display.update()

    # Regulando o FPS 
    clock.tick(60)