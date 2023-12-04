import pygame

class Player_obj(pygame.sprite.Sprite):
    def __init__(self,pos,lives,speed):
        super().__init__()
        self.lives = lives
        self.speed = speed
        self.image = pygame.image.load("images/niceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect(midbottom = pos)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self.get_input()
