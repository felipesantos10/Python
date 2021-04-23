#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#Falta concluir
import pygame
#Foi utilizado a biblioteca de jogos em especifico a função de musica
pygame.init()
#Dentro do load é colocado a musica
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()
