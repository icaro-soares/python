import sys

from settings import Settings
from ship import Ship

import pygame


class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamentos do jogo"""

    def __init__(self):
        # Inicializa o jogo e cria os recursos
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")


        self.ship = Ship(self)


    def run_game(self):
        # Inicaliza o loop principal do jogo
        while True:
            # Observa os eventos do teclado e do mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                # Redesenha a tela a cada passagem do loop
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()


                # Deixa a tela desenhada mais recente visível
                pygame.display.flip()
                self.clock.tick(60)

                if __name__ == '__main__':
                    # Cria uma instância do jogo e executa o jogo
                    ai = AlienInvasion()
                    ai.run_game()
