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

    def get_coords(self):
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
    if check_collision(object1.get_coords(), object2.get_coords()):
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
    The move method updates the position of the object based on its speed, and get_coords returns the current bounding box of the object.
    Main Loop:

    In the update function, the objects' positions are updated, and collisions are checked every 50 milliseconds using root.after(50, update). If a collision is detected, a message is printed in the console.
    How to Run:
    Run the code, and two rectangles will move across the canvas.
    When they collide, the message "Collision detected!" will be printed to the console.
    This is a simple example and can be expanded with more complex physics or responses when collisions are detected (like reversing direction or changing color).

5. CHATGPT DIALOGUE BELOW

    My question: write a very short example on how to bind user control movement using tkinter

    CHATGPT said: 

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


6. CHATGPT DIALOGUE BELOW

    My question: write the main method for what I have created (i pasted my code)

    CHATGPT Said: 

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
---

## Milestone 1: Setup, Planning, Design

**Source Assignment(s)**: `T12, T11, T10`

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![oludairoa_CRCcard.png](oludairoa_CRCcard.png "My CRC card")

️**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments: 

```
    Branch 1 name: oludairoa
    Branch 2 name: _____________
```
---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

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

Indicate what percentage of the project you have left to complete and how confident you feel. 

️**Completion Percentage**: `55%`

️**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

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
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

```
To use the program, use the arrow keys to move the green block around the canvas, while the blue block moves automatically. 
If the two blocks collide, they will shrink in size, and the game will end once any block's size reaches zero.
```

### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- (For partners) How well did you work with your partner? What made it go well? What made it challenging?


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