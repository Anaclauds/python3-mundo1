#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input() #na versão atual, diferente da versão do vídeo, necessita colocar o input
pygame.event.wait()



