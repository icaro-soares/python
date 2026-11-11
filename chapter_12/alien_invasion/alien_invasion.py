import sys

import pygame

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamentos do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria os recursos"""

        pygame.init()

        self.screen = pygame.display.set.mode((1200, 800))
        self.clock = pygame.time.clock()
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Inicaliza o loop principal do jogo"""

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """Desenha a tela a cada passagem do loop"""
            self.screen.fill(self.bg_color)

            """Deixa a tela desenhada mais recente visível"""
            pygame.display.flip()
            self.clock.tick(60)
            if __name__ == '__main__':

                ai = AlienInvasion()
                ai.run_game()