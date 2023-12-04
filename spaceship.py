import pygame
import sys
from Player import Player_obj

class Game:
    def __init__(self):
        global player
        player = Player_obj((screen_width / 2 - 20,screen_height - 20),3,5)
        self.player = pygame.sprite.GroupSingle(player)

    def run(self):
        #draw
        screen.fill((0,0,0))
        self.player.draw(screen)
        #update
        self.player.update()

if __name__ == '__main__':
    pygame.init()
    screen_width = 800
    screen_height = 500
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Spaceship shooter')
    running = True
    game = Game()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
        clock.tick(60)
        game.run()
        pygame.display.update()