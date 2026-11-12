import sys

import pygame

from blue_sky_settings import Settings

class BlueSky:
    def __init__(self):
        """Inicializador do game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_screen)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
