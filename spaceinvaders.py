import pygame
import Tilemap

def main(): 
    pygame.init()

    screen = pygame.display.set_mode((640,640))
    
    pygame.display.set_caption('Space Invaders')
    pygame.mouse.set_visible(0)
    # pygame.key.set_repeat(1,30)
    
    # background = Tilemap.Tilemap()
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
                
                # background.handle_input(event.key)
                
        screen.blit(background, (0,0))
        # background.render(screen)
        
        pygame.display.flip()
    

if __name__ == '__main__':
    main()