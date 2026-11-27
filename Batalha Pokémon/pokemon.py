import os
import pygame
import random
import time

HP_PLAYER = 100
HP_BOT = 100
meu_pokemon = ""
pokemon_rival = ""

def limpar(tempo=0):
    time.sleep(tempo)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

pygame.mixer.init()
pygame.mixer.music.load("OpeningTheme.mp3")
pygame.mixer.music.play(0)
time.sleep(1.7)
limpar()


print("█▀▀▄")
print("█▀▀▄")
print("▀▀▀ ")
limpar(0.65)

print("█▀▀▄ ▄▀▀▄")
print("█▀▀▄ █▀▀█")
print("▀▀▀  ▀  ▀")
limpar(0.55)

print("█▀▀▄ ▄▀▀▄ ▀█▀")
print("█▀▀▄ █▀▀█  █ ")
print("▀▀▀  ▀  ▀  ▀ ")
limpar(0.45)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀")
limpar(0.36)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █   ")
print("█▀▀▄ █▀▀█  █  █▀▀█ █   ")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀")
limpar(0.28)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀")
limpar(0.22)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀")
limpar(0.25)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄")
print("█▀▀▀")
print("▀   ")
limpar(0.16)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄ ▄▀▀▄")
print("█▀▀▀ █  █")
print("▀     ▀▀ ")
limpar(0.14)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄ ▄▀▀▄ █ ▄")
print("█▀▀▀ █  █ █▀▄")
print("▀     ▀▀  ▀ ▀")
limpar(0.10)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄ ▄▀▀▄ █ ▄ █▀▀▀")
print("█▀▀▀ █  █ █▀▄ █▀▀ ")
print("▀     ▀▀  ▀ ▀ ▀▀▀▀")
limpar(0.08)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄ ▄▀▀▄ █ ▄ █▀▀▀ █▀▄▀█")
print("█▀▀▀ █  █ █▀▄ █▀▀  █ ▀ █")
print("▀     ▀▀  ▀ ▀ ▀▀▀▀ ▀   ▀")
limpar(0.07)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄ ▄▀▀▄ █ ▄ █▀▀▀ █▀▄▀█ ▄▀▀▄")
print("█▀▀▀ █  █ █▀▄ █▀▀  █ ▀ █ █  █")
print("▀     ▀▀  ▀ ▀ ▀▀▀▀ ▀   ▀  ▀▀ ")
limpar(0.06)

print("█▀▀▄ ▄▀▀▄ ▀█▀ ▄▀▀▄ █    █  █ ▄▀▀▄")
print("█▀▀▄ █▀▀█  █  █▀▀█ █    █▀▀█ █▀▀█")
print("▀▀▀  ▀  ▀  ▀  ▀  ▀ ▀▀▀▀ ▀  ▀ ▀  ▀\n")
print("█▀▀▄ ▄▀▀▄ █ ▄ █▀▀▀ █▀▄▀█ ▄▀▀▄ █▄  █")
print("█▀▀▀ █  █ █▀▄ █▀▀  █ ▀ █ █  █ █ ▀▄█")
print("▀     ▀▀  ▀ ▀ ▀▀▀▀ ▀   ▀  ▀▀  ▀   ▀")

pygame.mixer.music.set_volume(0.49)

print()
time.sleep(0.7)
som = pygame.mixer.Sound("playsom.mp3")

input("Pressione ENTER para continuar! ")
print("— feito por q6uti :)")

som.play()
time.sleep(0.8)
pygame.mixer.music.stop()
limpar()
