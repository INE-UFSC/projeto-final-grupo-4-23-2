import pygame
from Button import *
#from ScreenObserver import *
from ScreenBase import ScreenBase
pygame.font.init()

class HomeScreen(ScreenBase):
    def __init__(self):
        super().__init__("Nome da Janela", 800, 600)  # Substitua "Nome da Janela" por seu título real
        self.initialize_screen() 
        button_spacing = 50
        button_size = 30
        self.__buttons = []

        for text, pos_y in [("Iniciar jogo", 210), ("Consultar ranking", 270 + button_spacing), ("Sair", 320 + 2 * button_spacing)]:
            font = pygame.font.SysFont('comicsansms', size=button_size)
            texto_surface = font.render(text, True, (0, 0, 0))
            largura_texto, altura_texto = texto_surface.get_size() 

            # Carrega a imagem do botão e redimensiona com base na largura do texto
            button = pygame.image.load("imagens/botao.png").convert_alpha()
            button = pygame.transform.scale(button, (largura_texto + 50, altura_texto + 50))  

            self.__buttons.append(
                Button(image=button, pos=(400, pos_y), text_input=text, font=font, base_color="white", hovering_color="green")
            )

        
        self.__observers = []

    def screen_view(self):
       

  
        
        #carregando imagens
        background_image = pygame.image.load("imagens/fundo_menu.jpg").convert()
        background_image = pygame.transform.scale(background_image, (self.width, self.height))
        mushroom_image = pygame.image.load("imagens/mushroom_cartoon.png").convert_alpha()  
        mushroom_image = pygame.transform.scale(mushroom_image, (500,500))

        #desenhando
        self.screen.blit(background_image, (0, 0))
        #self.screen.blit(mushroom_image, (50, 100))
  

        for button in self.__buttons:
            button.change_color(pygame.mouse.get_pos())

        for button in self.__buttons:
            button.update(self.screen)

 



