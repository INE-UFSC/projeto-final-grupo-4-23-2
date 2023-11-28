import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase

class RestrationScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.__text2_surface = None
        self.__text2_rect = None
        self.__label_surface = None
        self.__color = None
        self.__input_box = None
        self.initialize_screen()


    def screen_design(self):
        self.background_image = self.resource_manager.get_image("t1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        
        font = pygame.font.SysFont('comicsansms', size=30)
        self.text_surface = font.render("Insira um nome para o seu jogador ou", True, (255, 255, 255))
        self.__text2_surface = font.render("o nome já cadastrado", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(350, 60))
        self.__text2_rect = self.__text2_surface.get_rect(center=(350, 90))      
        
#######botões
        button_info = [("  Iniciar partida  ", 690, 250),("       Cadastrar      ", 690, 350), ("Consultar cadastros", 690, 450)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images=images_buttons, size_button=20)
##########caixa de texto
        label_text = "Nome: "
        self.__label_surface = font.render(label_text,True, (255,255,255))
        self.__input_box = pygame.Rect(150,300,400,30)
        self.__color = pygame.Color('white')
    
    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.__text2_surface, self.__text2_rect)
        self.screen.blit(self.__label_surface, (50, 300))
        pygame.draw.rect(self.screen, self.__color, self.__input_box)


        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())

            button.update(self.screen)