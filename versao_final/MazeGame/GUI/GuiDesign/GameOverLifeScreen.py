import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase

class GameOverLifeScreen(ScreenBase):
    def __init__(self, width=800, height=600):
        super().__init__(width, height)

        self.initialize_screen()

    def screen_design(self):
        background = self.resource_manager.get_image("purple.jpg")
        background = pygame.transform.scale(background, (self.width, self.height))

        clock = self.resource_manager.get_image("heart.png")
        clock = pygame.transform.scale(clock, (350, 250))
        clock_x = (self.width - clock.get_width()) // 2
        clock_y = (self.height - clock.get_height()) // 2

        font1 = pygame.font.SysFont('Tahoma', size=45)
        game_surface = font1.render("GAME OVER", True,(255,255,255))
        finish_surface= font1.render("suas vidas acabaram !", True,(255,255,255))
        game_rect = game_surface.get_rect(center=(400,50))
        finish_rect = finish_surface.get_rect(center=(400,110))

        self.screen.blit(background, (0, 0))
        self.screen.blit(game_surface,game_rect)
        self.screen.blit(finish_surface,finish_rect)
        self.screen.blit(clock, (clock_x, clock_y))

        button_info = [("Consultar ranking", 130, 550), ("   Nova partida   ", 400, 550), ("   Menu inicial   ", 650, 550)]
        button_images = ["button_blue.png", "button_blue.png", "button_blue.png"]

        self.create_buttons(button_info, images=button_images, size_button=16)

        

        for button in self.buttons:
            button.change_color(pygame.mouse.get_pos())

        for button in self.buttons:
            button.update(self.screen)
   
