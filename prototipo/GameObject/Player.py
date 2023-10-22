from GameObject import GameObject
import pygame
import os
from Constantes import ANIMATION_TIME, NEW_HEIGHT, NEW_WIDTH, PLAYER_SPEED




# Obtém o diretório do script Python atual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define a pasta de trabalho atual para o diretório do script (meu python não estava reconhecendo as pastas)
os.chdir(script_directory)


PLAYER_IMAGES = [
    pygame.image.load(os.path.join("sprites", "walk0001.png")),
    pygame.image.load(os.path.join("sprites", "walk0003.png")),
    pygame.image.load(os.path.join("sprites", "walk0005.png")),
    pygame.image.load(os.path.join("sprites", "walk0007.png")),
    pygame.image.load(os.path.join("sprites", "walk0009.png")),
    pygame.image.load(os.path.join("sprites", "walk0011.png")),
    pygame.image.load(os.path.join("sprites", "walk0013.png")),
    pygame.image.load(os.path.join("sprites", "walk0015.png")),
    pygame.image.load(os.path.join("sprites", "walk0017.png")),
    pygame.image.load(os.path.join("sprites", "walk0019.png")),
    pygame.image.load(os.path.join("sprites", "walk0021.png"))
]
# Redimensiona todas as imagens (a original tem 800 x 800)

for i in range(len(PLAYER_IMAGES)):
    PLAYER_IMAGES[i] = pygame.transform.scale(PLAYER_IMAGES[i], (NEW_WIDTH, NEW_HEIGHT))





class Player(GameObject):

    def __init__(self, position: (int, int), name: str, score: int, life: int, block: bool):
        super().__init__(position, block)
        self.__name = name
        self.__score = score
        self.__life = life
        self.__sprites = PLAYER_IMAGES
        self.__velocidade = 10 #quanto maior, mais rápido (diretamente proporcional)
        self.contagem_imagem = 0
        self.__imagem = self.__sprites[0]
    
  

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @property
    def life(self):
        return self.__life

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def imagem(self):
        return self.__imagem
    
    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    def draw_raccon(self, tela):

        self.contagem_imagem += 1 # Incrementa o contador de imagem a cada quadro

        for i in range(len(PLAYER_IMAGES)):
            if self.contagem_imagem < ANIMATION_TIME * (i + 1): # Verifica em qual parte da animação estamos
                self.imagem = self.__sprites[i] # Atualiza a imagem para a correspondente à parte atual da animação
                break

        if self.contagem_imagem >= ANIMATION_TIME * 11:
            self.contagem_imagem = 0  # reiniciada após atingir o limite/completar a animação
        tela.blit(self.imagem, self.position) #desenha a imagem na tela

    def handle_on_collision(self):
        return pygame.mask.from_surface(self.imagem)  #avaliando a colisão com a função mask.from_surface (analisa os pixels de forma precisa ao invés de pegar um retangulo)


    def move(self, key:str): #No pygame, a direção p cima é negativa
      
        if key == pygame.K_UP: #seta p cima pressionada
            self.position = (self.position[0], self.position[1] - self.velocidade)
        elif key == pygame.K_DOWN:
            self.position = (self.position[0], self.position[1] + self.velocidade)

        elif key == pygame.K_LEFT:
            self.position = (self.position[0] - self.velocidade, self.position[1])

        elif key == pygame.K_RIGHT:
            self.position = (self.position[0] + self.velocidade, self.position[1])


    def update(self):
        pass
