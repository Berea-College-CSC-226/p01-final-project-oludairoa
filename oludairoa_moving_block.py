import tkinter as tk
import random

class Block:
    def __init__(self, canvas, color, x, y, block_size=150):
        self.canvas = canvas
        self.color = color
        self.block_size = block_size
        self.x = x
        self.y = y
        self.block = self.canvas.create_rectangle(
            self.x - block_size // 2,
            self.y - block_size // 2,
            self.x + block_size // 2,
            self.y + block_size // 2,
            fill=self.color
        )

    def move(self, dx, dy):
        self.canvas.move(self.block, dx, dy)
        self.x += dx
        self.y += dy

    def get_coords(self):
        return self.canvas.coords(self.block)

    def shrink(self, shrink_size):
        self.block_size -= shrink_size
        self.block_size = max(self.block_size, 10)  # Prevent the block from disappearing
        self.canvas.coords(
            self.block,
            self.x - self.block_size // 2,
            self.y - self.block_size // 2,
            self.x + self.block_size // 2,
            self.y + self.block_size // 2
        )


class MovingBlock(Block):
    move_distance = 10
    directions = ["north", "east", "south", "west"]

    def __init__(self, canvas, x, y, screen_width, screen_height, block_size=50):
        super().__init__(canvas, "blue", x, y, block_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.path = random.choice(self.directions)

    def get_direction(self):
        if self.y + self.block_size // 2 >= self.screen_height:
            self.path = "north"
        if self.y - self.block_size // 2 <= 0:
            self.path = "south"
        if self.x - self.block_size // 2 <= 0:
            self.path = "east"
        if self.x + self.block_size // 2 >= self.screen_width:
            self.path = "west"
        elif random.random() > 0.95:
            self.path = random.choice(self.directions)

    def movement(self):
        if self.path == "north":
            self.move(0, -self.move_distance)
        elif self.path == "south":
            self.move(0, self.move_distance)
        elif self.path == "east":
            self.move(self.move_distance, 0)
        elif self.path == "west":
            self.move(-self.move_distance, 0)

        self.get_direction()