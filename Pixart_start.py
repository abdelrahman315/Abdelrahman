from turtle import Screen, Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

# Function for initializing the turtle's position and settings
def initialization(turta):
    '''Function which sets the speed, pencolor, and starting point of the turtle to start drawing'''
    turta.speed(1500)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)  
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

# Function to get the color based on a character
def get_color(char):
    if char == '0':
        return 'black'
    elif char == '1':
        return 'white'
    elif char == '2':
        return 'red'
    elif char == '3':
        return 'yellow'
    elif char == '4':
        return 'orange'
    elif char == '5':
        return 'green'
    elif char == '6':
        return 'yellowgreen'
    elif char == '7':
        return 'sienna'
    elif char == '8':
        return 'tan'
    elif char == '9':
        return 'gray'
    elif char == 'A':
        return 'darkgray'
    else:
        return None

# Function to draw a square that is filled in with a color
def draw_color(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for i in range(4):
        turta.forward(20)  
        turta.right(90)
    turta.end_fill()
    turta.forward(20)

# Function to draw a pixel based on the character input
def draw_pixel(char, turta):
    color = get_color(char)
    if color:
        draw_color(color, turta)

# Function to draw a line of pixels based on a string of characters
def draw_line_from_string(color_string, turta):
    for char in color_string:
        color = get_color(char)
        if color:
            draw_pixel(char, turta)
        else:
            
            return False
    return True

# Function to draw a square depending on what character you ask user yo use
def draw_shape_from_string(turta):
    while True:
        user_input = input("Enter a string of color codes (or press Enter to stop): ")
        if not user_input or not draw_line_from_string(user_input, turta):
            print("invalid character ")
        turta.penup()
        turta.goto(turta.xcor() - len(user_input) * ROWS, turta.ycor() - COLUMNS)  # Move to the next row
        turta.pendown()




#This function used to draw a grid 20 x 20 red and black
def draw_grid(turta):
    for row in range(ROWS):  
        if row % 2 == 0:
            draw_line_from_string('02020202020202020202', turta)  
        else:
            draw_line_from_string('20202020202020202020', turta)
                  
        turta.penup()
        turta.goto(turta.xcor() - ROWS * COLUMNS, turta.ycor() - COLUMNS )  
        turta.pendown()
    

# Function to draw shape from a text file you ask user to draw
def draw_shape_from_file(turta):
    file_path = input("Enter the text file you want to read: ")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                draw_line_from_string(line.strip(), turta)
                turta.penup()
                turta.goto(turta.xcor() - len(line.strip()) * ROWS, turta.ycor() - COLUMNS)  
                turta.pendown()
                
    except FileNotFoundError:
        print("File not found!")


if __name__ == "__main__":
    screen = Screen()
    turta = Turtle()
    
initialization(turta)
#draw_shape_from_string(turta)  
#draw_grid(turta)
draw_shape_from_file(turta)
input("")  # Keep the window open