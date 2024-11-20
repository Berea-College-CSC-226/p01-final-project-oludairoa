import pygame
from oludairoa_moving_block import MovingBlock
from oludairoa_moving_block import UserBlock

class Game:
    def __init__(self):
        """
        Game class for handling the game logic.
        """
        self.size = 800, 600
        self.shrink = 10
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#9CBEBA')
        self.clock = pygame.time.Clock()
        self.moving_block = MovingBlock(self.size, self.shrink)
        self.user_block = UserBlock(self.size, self.shrink)

    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            if pygame.sprite.spritecollide(self.user_block, [self.moving_block], False):
                pass
            elif pygame.sprite.spritecollide(self.moving_block, [self.user_block], False):
                pass
            else:
                self.moving_block.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.moving_block.surf, self.moving_block.rect)
                self.screen.blit(self.user_block.surf, self.user_block.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()

def main():
    """

    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()