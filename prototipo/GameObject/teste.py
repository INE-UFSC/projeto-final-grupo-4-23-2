import pygame

pygame.init()

# Obtém a lista de fontes instaladas
font_list = pygame.font.get_fonts()

for font in font_list:
    print(font)
