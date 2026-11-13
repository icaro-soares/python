import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        # Inicializa e cria recursos do jogo
        pygame.init()

        # Cria uma instância de Clock que garante a taxa de quadros
        self.clock = pygame.time.Clock()

        # Cria uma instância de Settings()
        self.settings = Settings()

        # Cria uma tela para o jogo
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Cria uma instância de Ship()
        self.ship = Ship(self)

        
    def run_game(self):
        # Inicia o loop principal do jogo

        while True:
            # Observa os eventos do mouse e teclado

            self._check_events()
            self._update_screen()

            # Quantidade de vezes que a tela atualiza a cada segundo
            self.clock.tick(60)

    def _check_events(self):
            # Responde as teclas pressionadas do mouse ou teclado
            for event in pygame.event.get():
                # Se o tipo do evento capturado for QUIT, o jogo encerra
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
            # Redesenha a tela com a cor designada
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Deixa a tela desenhada mais recentemente visível
            pygame.display.flip()
          

if __name__ == '__main__':
    # Cria uma instância do jogo e o executa
    ai = AlienInvasion()
    ai.run_game()
