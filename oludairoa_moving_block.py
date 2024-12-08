import pygame, random
import tkinter as tk

class MovingBlock(pygame.sprite.Sprite):

    move_distance = 10
    directions = ["north", "east", "south", "west"]

    def __init__(self, screen_size, shrink_size):
        """

        """

        self.screen_size = screen_size
        self.shrink_size = shrink_size
        super().__init__()
        self.surf = pygame.image.load('image/scottsgraybox.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (250, 250))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//4, self.screen_size[1]//4)
        self.path = random.choice(self.directions)
        self.position = [0,600]

    def get_direction(self):
        """

        """
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "north"
        if self.rect.top <= 0:
            self.path = "south"
        if self.rect.left <= 0:
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            self.path = "west"
        elif random.random() > .95:
            self.path = random.choice(self.directions)

    def movement(self):
        """

        """
        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)
            self.position[0] += self.move_distance

        self.get_direction()

    # create shrink method


class UserBlock(MovingBlock):
    def __init__(self, screen_size, shrink_size):

        super().__init__(screen_size, shrink_size)
        self.surf = pygame.image.load('image/greenbox_finalProject.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (250, 250))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.position = [800, 0]

# this function needs to be re-written to make the movement based on mouse drag, not arrow keys
    def movement(self):
        """

        """
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.rect.move_ip(self.mouse_x, self.mouse_y)