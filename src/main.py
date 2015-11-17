import pygame, sys
from game_objects import *
from pygame.locals import *

class Game:
    def __init__(self,clock,surface,movable_characters,main_player):
        self.clock = clock
        self.surface = surface
        self.movable_characters = movable_characters
        self.main_player = main_player

def initialize_game():
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((1200, 900), 0, 32)
    movable_characters = []
    main_player = MovableCharacter("P1",pygame.image.load, ["res/main_player/up.png", "res/main_player/right.png", "res/main_player/down.png", "res/main_player/left.png"])
    main_player.change_direction(main_player.current_direction, override_opt = True)
    movable_characters.append(main_player)
    return Game(clock,surface,movable_characters,main_player)

def keypress_event(event,main_player):
    if event.type == KEYDOWN:
        if main_player.moving: # Player's currently moving, ignore keypresses
			return;
        # Use change_direction instead of just changing the
        # variable since it also changes the sprite image
        main_player.moving = True
        if event.key == K_UP:
            main_player.change_direction(Direction.UP)
        elif event.key == K_RIGHT:
            main_player.change_direction(Direction.RIGHT)
        elif event.key == K_DOWN:
            main_player.change_direction(Direction.DOWN)
        elif event.key == K_LEFT:
            main_player.change_direction(Direction.LEFT)
        else:
            main_player.moving = False # If the player pushed an invalid key, don't move character.
# run the game loop
def game_loop():
    FPS = 30 
    game_instance = initialize_game()

    surface = game_instance.surface
    clock = game_instance.clock
    movable_characters = game_instance.movable_characters
    main_player = game_instance.main_player

    while True:
        surface.fill((10,10,10))
        for x in range(0, 1250, 50):
			for y in range(0, 950, 50):
				pygame.draw.circle(surface, (128, 128, 128), (x, y), 4, 0)

        for character in movable_characters:
            if character.moving:
                character.move()
                
            surface.blit(character.sprite, (character.x, character.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            keypress_event(event, main_player)

        pygame.display.update()
        clock.tick(FPS)
        

if __name__ == '__main__':
    game_loop()
