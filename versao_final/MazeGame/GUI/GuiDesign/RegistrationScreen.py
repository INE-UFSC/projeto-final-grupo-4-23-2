import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase

class RestrationScreen(ScreenBase):
    def __init__(self, width=800, height=400):
        super().__init__(width, height)
        self.initialize_screen()

    def screen_design(self):
        background_image = self.resource_manager.get_image("t1.jpg")
        background_image = pygame.transform.scale(background_image, (self.width, self.height))
        
        font = pygame.font.SysFont('comicsansms', size=25)
        text1_surface = font.render("Insira um nome para o seu jogador ou", True, (255, 255, 255))
        text2_surface = font.render("o nome já cadastrado", True, (255, 255, 255))
        text1_rect = text1_surface.get_rect(center=(350, 50))
        text2_rect = text2_surface.get_rect(center=(350, 80))      
        

##########caixa de texto
        label_text = "Nome: "
        label_surface = font.render(label_text,True, (255,255,255))
        input_box = pygame.Rect(150,200,400,30)
        color = pygame.Color('white')
    

        self.screen.blit(background_image, (0, 0))
        self.screen.blit(text1_surface, text1_rect)
        self.screen.blit(text2_surface, text2_rect)
        self.screen.blit(label_surface, (60, 200))
        pygame.draw.rect(self.screen, color, input_box)


#######botões
        button_info = [("Iniciar partida", 690, 150),("Cadastrar", 690, 250), ("Consultar cadastros", 690, 350)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images=images_buttons, size_button=15)

        for button in self.buttons:
            button.change_color(pygame.mouse.get_pos())

        for button in self.buttons:
            button.update(self.screen)