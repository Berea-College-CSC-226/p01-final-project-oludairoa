# CSC226 Final Project

**Author(s)**: Ayomide Oludairo
**Title**: `The Shrinking Moving Blocks Game`
**Objective**: `Two Moving Blocks are trapped in a border, one controlled by the user, the other as an NPC. When the 
blocks collide they shrink in size. The largest block at the end of the 5 minute timer is crowned the winner.`
**Google Doc Link**: https://docs.google.com/document/d/1uW7oIt1WSFsiUZfLIbqzTaMZ6qWyuRUnadt6qIY-lpY/edit?usp=sharing

---

## References 

1. Project inspired by T11: The Legends of Tuna: Breath of Catnip
2. T10: Intro to Classes
3. T12: Events and GUI's

4. CHATGPT DIALOGUE BELOW:

    My question: give me an example code handling collisions between objects using t kinter.

    ChatGPT said:
```
    Sure! Here's an example of how you can handle basic collisions between two objects using the tkinter library in Python. 
    This example creates a window with two rectangles that move on the canvas, and the program detects when they collide.

    import tkinter as tk

    # Function to check if two rectangles overlap
    def check_collision(rect1, rect2):
        x1, y1, x2, y2 = rect1
        x3, y3, x4, y4 = rect2
        return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)

    # Class to manage the movement of the objects
    class MovingObject:
    def __init__(self, canvas, color, x, y, width, height, dx, dy):
        self.canvas = canvas
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
        self.rect = canvas.create_rectangle(x, y, x + width, y + height, fill=color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.coords(self.rect, self.x, self.y, self.x + self.width, self.y + self.height)

    def get_coordinates(self):
        return self.x, self.y, self.x + self.width, self.y + self.height

    # Create the Tkinter window and canvas
    root = tk.Tk()
    root.title("Collision Detection Example")

    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    # Create two moving objects
    object1 = MovingObject(canvas, "blue", 50, 50, 50, 50, 5, 5)
    object2 = MovingObject(canvas, "red", 300, 200, 50, 50, -5, -5)

    # Function to update the movement and check for collisions
    def update():
        object1.move()
        object2.move()

    # Check if the two objects collide
    if check_collision(object1.get_coordinates(), object2.get_coordinates()):
        print("Collision detected!")

    # Repeat the movement every 50 milliseconds
    root.after(50, update)

    # Start the movement and collision detection
    update()

    # Start the Tkinter main loop
    root.mainloop()

    Explanation:
    Collision Detection:

    The function check_collision checks if the two rectangles overlap by comparing their coordinates (top-left and bottom-right corners). If any of the conditions of non-overlap are true, it returns False; otherwise, it returns True.
    Moving Objects:

    The MovingObject class represents an object on the canvas. It has attributes for its position (x, y), size (width, height), and movement speed (dx, dy).
    The move method updates the position of the object based on its speed, and get_coordinates returns the current bounding box of the object.
    Main Loop:

    In the update function, the objects' positions are updated, and collisions are checked every 50 milliseconds using root.after(50, update). If a collision is detected, a message is printed in the console.
    How to Run:
    Run the code, and two rectangles will move across the canvas.
    When they collide, the message "Collision detected!" will be printed to the console.
    This is a simple example and can be expanded with more complex physics or responses when collisions are detected (like reversing direction or changing color).
```

5. CHATGPT DIALOGUE BELOW

    My question: write a very short example on how to bind user control movement using tkinter

    CHATGPT said: 
```
    Certainly! Here's a very short example where a user can move a rectangle using the arrow keys in tkinter:

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    root.title("Move Rectangle")

    # Create a canvas
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # Create a rectangle on the canvas
    rect = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

    # Function to move the rectangle based on arrow key presses
    def move_rect(event):
        if event.keysym == 'Left':
            canvas.move(rect, -10, 0)
        elif event.keysym == 'Right':
            canvas.move(rect, 10, 0)
        elif event.keysym == 'Up':
            canvas.move(rect, 0, -10)
        elif event.keysym == 'Down':
            canvas.move(rect, 0, 10)

    # Bind the arrow keys to the move_rect function
    root.bind("<Left>", move_rect)
    root.bind("<Right>", move_rect)
    root.bind("<Up>", move_rect)
    root.bind("<Down>", move_rect)

    # Start the Tkinter event loop
    root.mainloop()
```

6. CHATGPT DIALOGUE BELOW

    My question: write the main method for what I have created (i pasted my code)

    CHATGPT Said: 
```
    Here's the main method that will run the game by initializing the Tkinter window, setting up the game, and starting the Tkinter event loop:

File 3: main.py (Main method to run the game)
python
Copy code
import tkinter as tk
from game import Game  # Import the Game class from game.py

def main():
    # Initialize the Tkinter root window
    root = tk.Tk()
    root.title("Block Collision Game")

    # Set up the game with a canvas size of 500x500
    game = Game(root, canvas_width=500, canvas_height=500)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
```

7. CHATGPT DIALOGUE BELOW

    My question: how could i modify the program so that only one block shrinks at a time. As it is right now both blocks shrink when they collide.

    ChatGPT said:
```
To modify the program so that only one block shrinks at a time, you can introduce a condition that checks which block should shrink based on the direction of the collision. You can choose to shrink the block that is "colliding into" the other block (e.g., based on which block is moving or which block overlaps the other one). This can be done by comparing the relative positions of the blocks and deciding which block to shrink.

Here's a possible way to implement this change:

Update the handle_collision() method in game.py:
python

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
Explanation:
Collision Detection: The handle_collision() method still detects when the two blocks overlap.
Conditional Shrinking: Once the collision is detected, we check which block is on the left or right (or whichever side you want to consider the "moving" block). If the user block is to the left of the NPC block, the user block shrinks; otherwise, the NPC block shrinks.
Handling Overlap: If both blocks are in the same position, you can choose either block to shrink. In this case, I've chosen to shrink the NPC block, but you could modify this if you'd like.
Key Changes:
Now, only one block shrinks at a time based on which block is considered the "moving" one (for example, the user block or the NPC block).
You could adjust the logic to make it shrink the "leading" block or whichever block moves first.
This approach will give you more control over the shrinking behavior and allow only one block to shrink upon collision.
```
---

**CRC Card(s)**:
  
[oludairoa_CRCcard.png](oludairoa_CRCcard.png "My CRC card")

**Branches**:

```
    Branch 1 name: oludairoa
    Branch 2 name: _____________
```
---

## Milestone 2: Code Setup and Issue Queue


```
    So far I have been working on creating the individual UserBlock and MovingBlock classes. I am working on first getting 
    them to load onto the screen. I have used several references such as the code for the game from teamwork eleven. 
    I plan to code a shrink method myself and manipulate the events of the game when the blocks collide. I feel like I'm
    where I should be, but I would like to figure things out sooner, rather than later. I am worried about possibly not 
    finishing in time, and if I will ask for help when needed. I feel like what I'm doing right now is easy, I just need 
    to use the references provided, and then enhance them and personalize them to the game that I am aiming to create.
```

---

## Milestone 3: Virtual Check-In


```
    I believe that I will be able to complete this project on time. Now that I have solved some of the errors, most of 
    what I have left to do is related to creating and implementing functions. Once that is done I can look back and add 
    any extra features I feel are necessary. While creating my project I focused more on the functions when I first started.
    Then I began trying to design an interface based on the functions. In other parts, (the shrinking), I needed to have an 
    already existing interface in order for me to know if what I coded would work correctly or not. I also have several 
    references, as well as similar teamwork assignments that do the tasks I want to do. 
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions 

```
To use the program, use the arrow keys to move the green block around the canvas, while the blue block moves automatically. 
If the two blocks collide, they will shrink in size, and the game will end once any block's size reaches zero.
```

### Errors and Constraints
check issues

### Reflection



```
I selected this project because I wanted to create a simple game. I thought of idea of a moving block game when I first 
stumbled upon something similar while scrolling on social media. I decided to ass my own spin by making one of the blocks
controlled by the user. My final project was not at all close to my initial design. I wanted to at first make an easy weather app,
but once I got this idea, this had to be my final output.

Through this process, I learned how to use Tkinter for handling graphics and events in Python. I also learned how to 
manage object movement and detect object collisions. It helped me better understand how to structure and organize a game project.
The hardest part was getting the blocks to shrink properly and ensuring the game ends when a block reaches size zero. 
There were some issues at first when I tried to use only pygame to complete my project. By being proactive and researching I 
was able to find a better way to do it with t kinter.
 
Next time, I would focus more on planning the game mechanics and refining the collision logic before starting to code.
I also need to be more consistent in my project. I had so many different ideas, and implementations of the same idea that
it was very stressful at times knowing exactly what my final project would end up looking like.
```