import time
import pygame

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("/home/naomi/alarm.clock/le_vent_nous_portera.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():  # wait for music to finish playing
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print('keypress detected')
            if event.key == pygame.K_2:
                print('ending music')
                pygame.mixer.music.fadeout(2000)
    time.sleep(1)
