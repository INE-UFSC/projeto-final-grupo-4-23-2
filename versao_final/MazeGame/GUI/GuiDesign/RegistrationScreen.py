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
        self.__typed_name = ""
        self.__font = None
        self.initialize_screen()

    def get_typed_name(self):
        return self.__typed_name
    
    @property
    def typed_name(self):
        return self.__typed_name
    
    @typed_name.setter
    def typed_name(self, name):
        self.__typed_name = name

    def screen_design(self):

        #Fundo
        self.background_image = self.resource_manager.get_image("t1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        
        #Textos
        self.__font = pygame.font.SysFont('comicsansms', size=30)
        self.text_surface = self.__font.render("Insira um nome para o seu jogador ou", True, (255, 255, 255))
        self.__text2_surface = self.__font.render("o nome já cadastrado", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=((self.width//3)+100, 60))
        self.__text2_rect = self.__text2_surface.get_rect(center=((self.width//3)+100, 90))    
        
#######botões
        button_info = [("  Iniciar partida  ", self.width-110,( self.height//3)+50 ),("       Cadastrar      ", self.width-110, ( self.height//3)+150), ("Consultar cadastros", self.width-110, ( self.height//3)+250)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images=images_buttons, size_button=self.width//40)
        
##########caixa de texto
        label_text = "Nome: "
        self.__label_surface = self.__font.render(label_text,True, (255,255,255))
        self.__input_box = pygame.Rect((self.width-(self.width-120), ( self.height//3)+100 ,(self.width//2)-70,35))
        self.__color = pygame.Color('white')
    
    def render(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.__text2_surface, self.__text2_rect)
        self.screen.blit(self.__label_surface, (self.width-(self.width-20),( self.height//3)+100))
        
        pygame.draw.rect(self.screen, self.__color, self.__input_box)
        self.screen.blit(self.__font.render(self.__typed_name, True, (0,0,0)), (125, ( self.height//3)+100) )

        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)