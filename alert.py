# -*- coding:utf-8 -*-
import pygame

pygame.mixer.init()
pygame.mixer.music.load(
    "/Users/Three/workSpace/python/project/publicHouse/alert.mp3")
music = pygame.mixer.music


def playMusic():
    music.play(-1, 0)


def stopMusic():
    music.stop()
