from Game.Player import Player
import pygame
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from Engine.Physics.CollisionPolygons.Square import Square



#######instanciando os objetos para teste


# Instancie a classe Player com os argumentos acima
player = Player(
    initial_position=Vector3(150, 500, 200),
    collision_polygons=[Square(8)],
    name="Victória",
    score=100,
    life=3
)
largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


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
    player.draw_player(tela)
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
