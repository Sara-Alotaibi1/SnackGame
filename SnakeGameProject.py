from tkinter import * # import all functions built-in modules in tkinter library
import random # define series of functions for generating/manipulating random integers

#---------------------------------------------------------------------------------------------------------------------------

# this part we defined the dimensions of The Game
Width = 800 #screen width
Highet = 800 #screen hight
SnakeSpeed = 200 #the speed of the snake
Space= 20 #space size of the screen
BodySize = 2 #the length of snake body
Scolor = "#FFFFFF" #snake color
Fcolor = "#FF0000" #food color
background = "#FFB6C1" #background color

#---------------------------------------------Snake creation------------------------------------------------------------------

# this class is for designing the snake
class Snake:

    def __init__(self):#sepcial method that run when the instance of the class is created
        self.body_size = BodySize #initialize the Snake object by setting the body_size attribute to the value of the BodySize constant
        #create two empty list for the snake body
        self.coordinates = []
        self.squares = []

        for i in range(0, BodySize):
            self.coordinates.append([0, 0])#each time the snake eats the new omject will be added in the end of the list

        for x, y in self.coordinates:#to create the body size number of rectangles on canvase object
            square = canvas.create_rectangle(
                x, y, x + Space, y + Space,
                fill=Scolor, tag="snake")
            self.squares.append(square)

#--------------------------------------------Food creation--------------------------------------------------------------------
# Class to design the food
class Food:

    def __init__(self):
        # Generating food randomly anywhere in the game
        x = random.randint(0,
                           (Width / Space) - 1) * Space
        y = random.randint(0,
                           (Highet / Space) - 1) * Space

        self.coordinates = [x, y]

        # Giving shape of the food
        canvas.create_oval(x, y, x + Space, y +
                           Space, fill=Fcolor, tag="food")

#----------------------------------------------Movment-------------------------------------------------------------------------

# Function to check the next move of snake
def next_turn(snake, food): # this function takes two arguments snake object and food object
    x, y = snake.coordinates[0] # checks the position of the snake's head

    if direction == "up":
        y -= Space
    elif direction == "down":
        y += Space
    elif direction == "left":
        x -= Space
    elif direction == "right":
        x += Space

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + Space,
              y + Space, fill=Scolor)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        Scorelabel.config(text="Points:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    # if collision of the snake happens then
    # game over function is called
    if check_collisions(snake):
        game_over()

    else:
        window.after(SnakeSpeed, next_turn, snake, food)

#-------------------------------------directions--------------------------------------------------------------------------------------

# Function to control direction of snake
def change_direction(new_direction):#function takes a single argument
    global direction#declaring the direction variable as global so that it can be modified within the function.

    # check the value of new_direction.
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# function to check snake's collision and position
def check_collisions(snake):
    # Taking the coordinates of the snake head
    x, y = snake.coordinates[0]

    # The function returns true if the collision occurs
    if x < 0 or x >= Width:
        return True
    elif y < 0 or y >= Highet:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to control everything
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2,
                       canvas.winfo_height() / 2,
                       font=('consolas', 70),
                       text="GAME OVER", fill="red",
                       tag="gameover")



window =Tk()#CREATE TK OBJECT
window.title("Snake game ")# Giving title to the window

score = 0 #initializes the score to zero
direction = 'down'

# Display of Points Scored in Game
#create Label object to display the score
Scorelabel = Label(window, text="Points:{}".format(score),font=('consolas', 20))
Scorelabel.pack()

#Canvas object to display the game elements(snake,food,score...)
canvas = Canvas(window, bg=background,
                height=Highet, width=Width)
canvas.pack()

window.update()# refresh the window

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))#to center the window

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#bind functions to spesfic events
window.bind('<Left>',
            lambda event: change_direction('left'))#anonumes function
window.bind('<Right>',
            lambda event: change_direction('right'))
window.bind('<Up>',
            lambda event: change_direction('up'))
window.bind('<Down>',
            lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()

