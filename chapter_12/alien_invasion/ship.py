import os
import pygame


class Ship:
    """Classe para cuidar da espaçonave"""
    def __init__(self, ai_game):
        # Inicializa a espaçonave e define posição inicial
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Obtém o caminho absoluto da pasta onde está o ship.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Constrói o caminho completo até a imagem (ajuste 'images' se sua pasta for no singular 'image')
        image_path = os.path.join(current_dir, 'images', 'ship.bmp')

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        
        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        # Desenha a espaçonave em sua localização atual
        self.screen.blit(self.image, self.rect)
