import pygame
import Tileset
import Player

class Tilemap(object):
    def __init__(self):
        
        self.tileset = Tileset.Tileset('img/tileset.png', (255, 0, 255), 32, 32)
        self.tileset.add_tile('fighter', 200, 50)
        
        
    
    
        self.camera_x = 0
        self.camera_y = 0
        
        self.player = Player.Player()
        
    def render(self, screen):
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0,0,0))
        
        screen.blit(self.tileset.image, (self.tileset.tile_width, self.tileset.tile_height))
    
        self.player.render(screen)
        
        
    def handle_input(self, key):
        self.player.handle_input(key)