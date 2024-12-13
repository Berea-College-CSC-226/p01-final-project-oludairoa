import tkinter as tk
from oludairoa_Blocks import MovingBlock
from oludairoa_Blocks import UserControlledBlock

class Game:
    def __init__(self, root, canvas_width=500, canvas_height=500):
        self.root = root
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        # Initialize the blocks
        self.user_block = UserControlledBlock(self.canvas, canvas_width // 4, canvas_height // 2, block_size=50)
        self.npc_block = MovingBlock(self.canvas, canvas_width * 3 // 4, canvas_height // 2, canvas_width, canvas_height, block_size=50)

        self.root.bind("<Left>", self.user_block.move_left)
        self.root.bind("<Right>", self.user_block.move_right)
        self.root.bind("<Up>", self.user_block.move_up)
        self.root.bind("<Down>", self.user_block.move_down)

        self.update_game()

    def check_collision(self):
        user_coords = self.user_block.get_coordinates()
        npc_coords = self.npc_block.get_coordinates()

        if (
            user_coords[2] > npc_coords[0] and user_coords[0] < npc_coords[2] and
            user_coords[3] > npc_coords[1] and user_coords[1] < npc_coords[3]
        ):
            self.handle_collision()

    def handle_collision(self):
        user_coords = self.user_block.get_coordinates()
        npc_coords = self.npc_block.get_coordinates()

        # Check which block is colliding into the other (based on position and movement)
        if user_coords[2] > npc_coords[0] and user_coords[0] < npc_coords[2] and \
                user_coords[3] > npc_coords[1] and user_coords[1] < npc_coords[3]:

            # Shrink only the user block if it is on the left of the NPC block
            if self.user_block.x < self.npc_block.x:
                self.user_block.shrink(5)
            # Shrink only the NPC block if it is on the left of the user block
            elif self.npc_block.x < self.user_block.x:
                self.npc_block.shrink(5)
            # If both blocks are overlapping (same position), shrink only the NPC block (or choose whichever block)
            else:
                self.npc_block.shrink(5)

    def check_game_over(self):
        """
        Check if any block has reached a size of 0. If so, end the game.
        """
        if self.user_block.block_size <= 0 or self.npc_block.block_size <= 0:
            self.root.destroy()  # Close the Tkinter window to end the game
            print("Game Over!")  # Print game over message to console

    def update_game(self):
        self.npc_block.movement()  # NPC block moves automatically
        self.check_collision()  # Check for collisions
        self.check_game_over()  # Check if the game should end
        self.root.after(50, self.update_game)

def main():
    root = tk.Tk()
    root.title("Block Collision Game")

    game = Game(root, canvas_width=500, canvas_height=500)

    root.mainloop()

if __name__ == "__main__":
    main()