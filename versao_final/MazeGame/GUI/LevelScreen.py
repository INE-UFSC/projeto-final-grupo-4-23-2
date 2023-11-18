import pygame
from MazeGame.GUI.ScreenBase import ScreenBase


class LevelScreen(ScreenBase):
    def __init__(self, width= 800, height=400):
        super().__init__( width, height)
        self.initialize_screen()


    def screen_design(self):
        background_image = self.resource_manager.get_image("t1.jpg")
        background_image = pygame.transform.scale(background_image, (self.width, self.height))
        
        font = pygame.font.SysFont('comicsansms', size=30)
        text_surface = font.render("Escolha seu nível", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 50))

        self.screen.blit(background_image, (0, 0))
        self.screen.blit(text_surface, text_rect)

        # Adicionando cogumelos nas bordas
        mushroom_image = self.resource_manager.get_image("mushroom.png")
        mushroom_image = pygame.transform.scale(mushroom_image, (200, 200))

        self.screen.blit(mushroom_image, (1,200))
        self.screen.blit(mushroom_image, (600,200))


        button_info = [("Fácil", 400, 150), ("Intermediário", 400, 250), ("Difícil", 400, 350)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images=images_buttons, size_button=20)



        for button in self.buttons:
            button.change_color(pygame.mouse.get_pos())

        for button in self.buttons:
            button.update(self.screen)