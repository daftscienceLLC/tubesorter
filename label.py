import pygame 
from constants import *
import sys

sys.dont_write_bytecode = True

class Label(pygame.sprite.Sprite):

    def __init__(   self, 
                    screen,
                    text=None, 
                    bg_color=CLOUD,
                    transparent = False,
                    font_color=PURPLE, 
                    font=None, 
                    font_size=24,
                    background_size=None, 
                    center=None, 
                    align="Center"):

        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.Surface(self.screen.get_size())
        self.font = pygame.font.SysFont(font, font_size)
        self.text = text
        self.padding = 6
        self.transparent = False
        self.fgColor = font_color
        self.bgColor = bg_color
        self.align = align
        if center:
            self.center = center
        else:
            self.center = (self.background.get_width()/2, self.background.get_height()/2)
        if background_size:
            self.size = background_size
        else:    
            self.size = (self.background.get_width(), 20)
            
        

    def update(self):
        self.image = pygame.Surface(self.size)
        if self.transparent:
            self.image.fill(TRANSPARENT)
        else:
            self.image.fill(self.bgColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        if self.align =='left':
            fontRect = fontSurface.get_rect()
            bg_rect = self.image.get_rect()
            fontRect.left = bg_rect.left
            self.image.blit(fontSurface, fontRect)
        elif self.align =='right':
            fontRect = fontSurface.get_rect()
            bg_rect = self.image.get_rect()
            fontRect.right = bg_rect.right
            self.image.blit(fontSurface, fontRect)
        else:
            xPos = (self.image.get_width() - fontSurface.get_width())/2
            yPos = (self.image.get_height() - fontSurface.get_height())/2
            self.image.blit(fontSurface, (xPos, yPos))

        self.rect = self.image.get_rect()
        self.rect.center = self.center