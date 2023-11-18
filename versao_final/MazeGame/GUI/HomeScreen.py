import pygame
from MazeGame.GUI.Button import *
from MazeGame.GUI.ScreenBase import ScreenBase
from Engine.Structs.ResourceManager import ResourceManager

class HomeScreen(ScreenBase):
    def __init__(self):
        super().__init__(800, 600)  # Substitua "Nome da Janela" por seu título real
        self.initialize_screen() 
        #button_spacing = 50
        #button_size = 30
        #self.resource_manager = ResourceManager()

        '''
        for text, pos_y in [("Iniciar jogo", 210), ("Consultar ranking", 270 + button_spacing), ("Sair", 320 + 2 * button_spacing)]:
            font = pygame.font.SysFont('comicsansms', size=button_size)
            texto_surface = font.render(text, True, (0, 0, 0))
            largura_texto, altura_texto = texto_surface.get_size()

            # Carrega a imagem do botão e redimensiona com base na largura do texto
            button = self.resource_manager.get_image(name="botao.png")
            button = pygame.transform.scale(button, (largura_texto + 50, altura_texto + 50))  

            self.buttons.append(
                Button(image=button, pos=(400, pos_y), text_input=text, font=font, base_color="white", hovering_color="green")
            )
        '''

    def screen_design(self):
        #carregando imagens
        background_image = self.resource_manager.get_image("background_menu.jpg")
        background_image = pygame.transform.scale(background_image, (self.width, self.height))


        #desenhando
        self.screen.blit(background_image, (0, 0))
        button_info = [("Iniciar", 400, 210), ("Consultar ranking", 400, 320), ("Sair", 400, 420 )]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        #images_buttons = [None, None, None]
        self.create_buttons(button_info,images_buttons,size_button=25)

        for button in self.buttons:
            button.change_color(pygame.mouse.get_pos())

        for button in self.buttons:
            button.update(self.screen)
