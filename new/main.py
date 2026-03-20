import pygame

class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/fighter.png')
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_height() - 33)
        
    def update(self):
        self.rect.center
            
def main(): 
    pygame.init()

# Display
    screen = pygame.display.set_mode((640,640))
    pygame.display.set_caption('Space Invaders')
    pygame.mouse.set_visible(0)
    # pygame.key.set_repeat(1,30)

# Entities


    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    clock = pygame.time.Clock()
        
    running = True

    while running:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                
        screen.blit(background, (0,0))        
        pygame.display.flip()
    

if __name__ == '__main__':
    main()