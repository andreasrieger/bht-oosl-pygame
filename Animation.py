import pygame

class Animation(object):
    def __init__(self, image, start_x, start_y, num, width, height, duration):
        self.image = image
        self.start_x = start_x       
        self.start_y = start_y
        self.num = num
        self.width = width
        self.height = height
        self.duration = duration
        self.time = 0
        self.current = 0
        
    def render(self, screen, pos):
        screen.blit(self.image, pos, pygame.Rect(self.start_x + (self.width * self.current), self.start_y, self.width, self.height))
        
    def update(self, time=1):
        self.time += time
        if self.time > self.duration:
            self.time = 0
            self.current += 1
            if self.current >= self.num:
                self.current = 0