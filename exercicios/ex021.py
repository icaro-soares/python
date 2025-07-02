#Faça um programa em python que leia e reproduza um arquivo mp3
import pygame


musica = pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(musica)
pygame.mixer.music.stop()
