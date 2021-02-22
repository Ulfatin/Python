# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:43:35 2020

@author: urfi
"""

import pygame,sys,os
from pygame.locals import *    # load constants
os.environ['SDL_VIDEODRIVER']='windlib'

red=(255,0,0)
pygame.init()

#setup window
window=pygame.display.set_mode((400,300))
pygame.display.set_caption("Slither.eat - Snake Game")
screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()
while True:
  for event in pygame.event.get():
    print(event)
    if event.type=="QUIT":
      pygame.quit()
      sys.exit()
  pygame.display.update()


  print("Slither.eat - The Snake Game")
  pass