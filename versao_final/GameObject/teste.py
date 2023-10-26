from Player import Player
import pygame

largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

player = Player((4, 4), "victória", 100, 5, block=None)
relogio = pygame.time.Clock()

executando = True

while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    keys = pygame.key.get_pressed()  # Captura o estado das teclas
    
    if keys[pygame.K_UP]:
        player.move(pygame.K_UP)
    if keys[pygame.K_DOWN]:
        player.move(pygame.K_DOWN)
    if keys[pygame.K_LEFT]:
        player.move(pygame.K_LEFT)
    if keys[pygame.K_RIGHT]:
        player.move(pygame.K_RIGHT)
        
    tela.fill(PRETO)
    player.draw_raccon(tela)
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
