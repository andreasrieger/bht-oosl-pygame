import pygame
import Utils
import Animation

class Player(object):
    def __init__(self):
        self.anim_image_right = Utils.load_image('img/fighter.png', (255, 0, 255))
        self.anim_right = Animation.Animation(self.anim_image_right, 100, 0, 1, 66, 66, 15)
        
        self.anim_image_left = pygame.transform.flip(self.anim_image_right, True, False)
        self.anim_left = Animation.Animation(self.anim_image_left, 100, 0, 1, 66, 66, 15)
        
        self.pos_x = 10
        self.pos_y = 10        
        self.dir = 0
        self.walking = False
        
    def handle_input(self, key):
        # Linke Pfeiltaste wird gedrückt:
        if key == pygame.K_LEFT:
            # x-Position der Spielfigur anpassen,
            # die Blickrichtung festlegen
            # und den Laufen-Zustand einschalten.
            self.pos_x -= 1
            self.dir = -1
            self.walking = True
 
        # Und nochmal für die rechte Pfeiltaste.
        if key == pygame.K_RIGHT:
            self.pos_x += 1
            self.dir = 1
            self.walking = True
            
    def render(self, screen):
        # Die Blickrichtung ist links:
        if self.dir == -1:
            # Wenn der Spieler die linke oder rechte Pfeiltaste gedrückt hat sind wir am laufen,
            if self.walking:                
                # nur dann die Animation updaten.
                self.anim_left.update()
            # Blickrichtung links rendern.
            self.anim_left.render(screen, (self.pos_x, self.pos_y))   
        else:
            # Und das gleiche nochmal für rechts:
            if self.walking:
                self.anim_right.update()
            self.anim_right.render(screen, (self.pos_x, self.pos_y))
 
        # De Laufen-Zustand zurücksetzen, im nächsten Frame bleiben wir stehen.
        self.walking = False