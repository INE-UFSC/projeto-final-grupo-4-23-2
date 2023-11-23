import pygame
class Button():
    def __init__(self, image, pos: tuple, text_input: str, font: str, base_color, hovering_color):
        self.__image = image
        self.__font = font
        self.__pos = pos #posição x e y 
        self.__base_color = base_color
        self.__hovering_color = hovering_color
        self.__text_input = text_input
        self.__text = self.__font.render(self.__text_input, True, self.__base_color)
        if self.__image is None:
            self.__image = self.__text
        self.__rect = self.__image.get_rect(center=(self.__pos[0], self.__pos[1]))
        self.__text_rect = self.__text.get_rect(center=(self.__pos[0], self.__pos[1]))


    def update(self, screen):
        # Atualiza a tela com a imagem e o texto
        if self.__image is not None:
            screen.blit(self.__image, self.__rect)
        screen.blit(self.__text, self.__text_rect)

    def check_input(self, position):
        if position[0] in range(self.__rect.left, self.__rect.right) and position[1] in range(self.__rect.top, self.__rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.__rect.left, self.__rect.right) and position[1] in range(self.__rect.top, self.__rect.bottom):
            self.__text = self.__font.render(self.__text_input, True, self.__hovering_color)
        else:
            self.__text = self.__font.render(self.__text_input, True, self.__base_color)

    def clicked(self, mouse_pos):
        x, y, width, height = self.__rect
        is_hovered = x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height
        is_left_click = pygame.mouse.get_pressed()[0] == 1 #indice 0 = botão esquerdo do mouse
        return is_hovered and is_left_click #retorna true se estiver em cima do botão e o botão esquerdo for pressionado