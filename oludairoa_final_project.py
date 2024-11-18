import pygame
from oludairoa_moving_block import MovingBlock

class Game:
    def __init__(self):
        """
        Game class for handling the game logic.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#9CBEBA')
        self.clock = pygame.time.Clock()
        self.moving_block = MovingBlock(self.size)
        # self.user_block =

    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            if pygame.sprite.spritecollide(self.moving_block, [self.tacocat], False):

            else:

                self.moving_block.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.moving_block.surf, self.moving_block.rect)
                self.screen.blit(self.tacocat.surf, self.tacocat.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()
