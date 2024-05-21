import pygame
from personagens import Personagem
from obstaculo import Obstaculo

pygame.init()
pygame.mixer.init()
#Construindo a tela
tela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Jogo do chinbinho")
tela.fill((117, 75, 19))

musica = pygame.mixer.Sound("Borboletinha.mp3")

pontuacao = 0
vidas = 5

# Carregando imagens
fundo = Personagem("imagem/fundo.png", 1000, 700, 0, 0 )
borboleta = Personagem("imagem/borboleta.png", 190, 190, 400, 510 ) 


# Carregando imagens
# Criando personagens
lista_itens = [ 
Obstaculo("imagem/açucar.png", 50, 60, 0, 710 ),
Obstaculo("imagem/chocolate.png", 50, 60, 0, 710),
Obstaculo("imagem/colher.png", 50, 60, 0, 710 ),
Obstaculo("imagem/leite.png", 50, 60, 0, 710 ),
Obstaculo("imagem/manteiga.png", 50, 60, 0, 710 )
]

lista_ruim = [Obstaculo("imagem/alface.png", 50, 60, 0, 710 ),
Obstaculo("imagem/pimenta.png", 50, 60, 0, 710),
Obstaculo("imagem/sapo.png", 50, 60, 0, 710 ),
]



# Criando um relógio para configurar o fps
clock = pygame.time.Clock()

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if vidas >= 0:
                pygame.MOUSEBUTTONDOWN:
                    vidas = 5
                    pontuacao = 0
            pass

    musica.play()

    fundo.desenhar(tela)

    for obstaculo in lista_ruim:
        obstaculo.movimenta()
        obstaculo.desenhar(tela)

        if borboleta.mascara.overlap(obstaculo.mascara,(obstaculo.posiçãoX-borboleta.posiçãoX, obstaculo.posiçãoY-borboleta.posiçãoY,)):
            obstaculo.posiçãoY = 1050
            pontuacao = pontuacao - 1
            vidas = vidas - 1

    for obstaculo in lista_itens:
        obstaculo.movimenta()
        obstaculo.desenhar(tela)

        if borboleta.mascara.overlap(obstaculo.mascara,(obstaculo.posiçãoX-borboleta.posiçãoX, obstaculo.posiçãoY-borboleta.posiçãoY,)):
            obstaculo.posiçãoY = 1050
            pontuacao = pontuacao + 1

    borboleta.desenhar(tela)
    borboleta.andar()
    
    fonte = pygame.font.SysFont("Cooper Black",28, False, False)

    texto_pontuacao = fonte.render(f"Pontuação:{pontuacao} ", True, (0, 0, 0))
    texto_vidas = fonte.render(f"Vidas:{vidas} ", True, (240, 22, 120))

    tela.blit(texto_pontuacao,(30,630))
    tela.blit(texto_vidas,(30,660))


    # Atualizando a tela
    pygame.display.update()

    # Regulando o FPS 
    clock.tick(60)