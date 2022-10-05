# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from textwrap import fill
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    for x in range(400, 600, 25):
        draw_maple_tree(canvas, x, 275, 10)
    
    for x in range(350, 650, 25):
        draw_maple_tree(canvas, x, 250, 10)

    for x in range(100, 750, 50):
        draw_maple_tree(canvas, x, 225, 15)
    
    draw_pine_tree(canvas, 290, 240, 20)
    draw_barn(canvas, 350, 175, 30)

    for x in range(300, scene_width, 60):
        draw_maple_tree(canvas, x, 180, 20)

    draw_barn(canvas, 200, 150, 30)
    draw_pine_tree(canvas, 350, 180, 20)

    draw_pine_tree(canvas, 110, 240, 20)
    draw_pine_tree(canvas, 160, 250, 20)  

    # left side of church
    draw_barn(canvas, 150, 175, 30)

    for x in range(25, 200, 60):
        draw_maple_tree(canvas, x, 175, 20)

    draw_barn(canvas, 175, 125, 30)
    draw_pine_tree(canvas, 125, 225, 20)
    draw_pine_tree(canvas, 175, 175, 20)

    for x in range(350, scene_width, 80):
        draw_maple_tree(canvas, x, 125, 30)

    # larger pine left of screen
    draw_pine_tree(canvas, 75, 250, 50)

    for x in range(10, 200, 80):
        draw_maple_tree(canvas, x, 125, 30)

    for x in range(60, 200, 80):
        draw_maple_tree(canvas, x, 75, 30)

    for x in range(400, scene_width, 100):
        draw_maple_tree(canvas, x, 100, 40)

    draw_church(canvas, 275, 175, 45)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
    
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="steelBlue4")

    draw_cloud(canvas, 150, 415, 30)
    draw_cloud(canvas, 300, 350, 60)    
    draw_cloud(canvas, 525, 430, 40)

def draw_cloud(canvas, bottom_x, bottom_y, size):

    # Draw initial cloud. First row
    upper_x = bottom_x + size
    upper_y = bottom_y + size
    offset = size / 2

    for x in range(4):
        draw_oval(canvas, bottom_x + (x * offset), bottom_y, upper_x + (x * offset), upper_y, outline="slateGray1", fill="slateGray1")

    # Diagonal offset. Second row
    bottom_row_lower_x = bottom_x - offset
    bottom_row_lower_y = bottom_y - offset
    bottom_row_upper_x = upper_x - offset
    bottom_row_upper_y = upper_y - offset

    for x in range(4):
        draw_oval(canvas, bottom_row_lower_x + (x * offset), bottom_row_lower_y, bottom_row_upper_x + (x * offset), bottom_row_upper_y, outline="slateGray1", fill="slateGray1")
  

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="darkGreen")

    draw_oval(canvas, 0, 0, 400, 210, outline="darkGreen", fill="darkGreen")
    draw_oval(canvas, 275, 0, 750, 270, outline="darkGreen", fill="darkGreen")


def draw_church(canvas, base_bottom_right_x, base_bottom_right_y, size):

    # Church Base
    base_upper_left_x = base_bottom_right_x - size
    base_upper_left_y = base_bottom_right_y + size

    draw_rectangle(canvas, base_bottom_right_x, base_bottom_right_y, base_upper_left_x, base_upper_left_y, fill="white")

    # Church steeple rectangle
    rectangle_bottom_right_x = base_bottom_right_x - (size / 5)
    rectangle_bottom_right_y = base_upper_left_y
    rectangle_upper_left_x = base_upper_left_x + (size / 5)
    rectangle_upper_left_y = rectangle_bottom_right_y + size
      
    draw_rectangle(canvas, rectangle_bottom_right_x, rectangle_bottom_right_y, rectangle_upper_left_x, rectangle_upper_left_y, fill="white")

    # Church triangle above base
    center_x = (base_bottom_right_x + base_upper_left_x) / 2
    
    triangle_top = rectangle_bottom_right_y + ((rectangle_upper_left_y - rectangle_bottom_right_y) / 2) 
    triangle_left_bottom_x = base_upper_left_x
    triangle_left_bottom_y = base_upper_left_y
    triangle_left_right_x = base_bottom_right_x
    triangle_right_bottom_y = base_upper_left_y

    draw_polygon(canvas, 
                center_x, 
                triangle_top,
                triangle_left_bottom_x, 
                triangle_left_bottom_y, 
                triangle_left_right_x, 
                triangle_right_bottom_y,
                outline="gray20", 
                width=1,
                fill="white")

    # Church steeple point
    steeple_top = rectangle_upper_left_y + size
    steeple_left_bottom_x = center_x - (size / 10)
    steeple_left_bottom_y = rectangle_upper_left_y
    steeple_left_right_x = center_x + (size / 10)
    steeple_right_bottom_y = rectangle_upper_left_y
   
    draw_polygon(canvas, 
                 center_x, 
                 steeple_top,
                 steeple_left_bottom_x, 
                 steeple_left_bottom_y, 
                 steeple_left_right_x, 
                 steeple_right_bottom_y,
                 outline="gray20", 
                 width=1,
                 fill="white")
    
    # Draw church door
    door_bottom_right_x = center_x + (size / 10)
    door_bottom_right_y = base_bottom_right_y
    door_upper_left_x = center_x - (size / 10)
    door_upper_left_y = base_bottom_right_y + (size / 2)

    draw_rectangle(canvas, door_bottom_right_x, door_bottom_right_y, door_upper_left_x, door_upper_left_y, fill="gray")


def draw_barn(canvas, base_bottom_right_x, base_bottom_right_y, size):
    barn_colors = ["brown", "brown3", "brown4", "orangeRed3", "orangeRed4", "sienna","sienna4"]
    color = random.choice(barn_colors)

    # Barn Base
    base_upper_left_x = base_bottom_right_x - size
    base_upper_left_y = base_bottom_right_y + size

    draw_rectangle(canvas, base_bottom_right_x, base_bottom_right_y, base_upper_left_x, base_upper_left_y, fill=color)

    # Barn triangle above base
    center_x = (base_bottom_right_x + base_upper_left_x) / 2
    
    triangle_top = base_upper_left_y + (size / 2) 
    triangle_left_bottom_x = base_upper_left_x
    triangle_left_bottom_y = base_upper_left_y
    triangle_left_right_x = base_bottom_right_x
    triangle_right_bottom_y = base_upper_left_y

    draw_polygon(canvas, 
                center_x, 
                triangle_top,
                triangle_left_bottom_x, 
                triangle_left_bottom_y, 
                triangle_left_right_x, 
                triangle_right_bottom_y,
                outline="gray20", 
                width=1,
                fill=color)

    interval = int(size / 5)
    for x in range(base_upper_left_x, base_bottom_right_x, interval):
        draw_line(canvas, x, base_upper_left_y, x, base_bottom_right_y, fill="black")

def draw_pine_tree(canvas, peak_x, peak_y, size):
    """Draw one pine tree at location (peak_x, peak_y)
       Size is the width of the skirt of the pine tree.
       Sizing in multiples of seven works best. """

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - (size / 2) # left half of tree #70
    skirt_right = peak_x + (size / 2) # right half of tree
    skirt_bottom = peak_y - (size * 3)
    trunk_left  = peak_x - (size / 7)
    trunk_right = peak_x + (size / 7)
    trunk_bottom = peak_y - (size * 3.5)

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")


def draw_maple_tree(canvas, bottom_x, bottom_y, size):

    fall_colors = ["orange", "orangeRed1", "orangeRed2", "orangeRed3", "orangeRed4", 
                   "sienna", "sienna1", "sienna2", "sienna3", "sienna4", 
                   "darkOrange", "darkOrange1", "darkOrange2", "darkOrange3", "darkOrange4",
                   "darkGoldenRod1", "darkGoldenRod2", "darkGoldenRod3", "darkGoldenrod4",
                   "oliveDrab4", "darkOliveGreen"]

    # Draw initial cloud. First row
    upper_x = bottom_x + size
    upper_y = bottom_y + size
    offset = size / 2

    for x in range(2):
        color = random.choice(fall_colors)
        draw_oval(canvas, bottom_x + (x * offset), bottom_y, upper_x + (x * offset), upper_y, outline=color, fill=color)

    # Diagonal offset. Second row
    bottom_row_lower_x = bottom_x - offset
    bottom_row_lower_y = bottom_y - offset
    bottom_row_upper_x = upper_x - offset
    bottom_row_upper_y = upper_y - offset

    for x in range(4):
        color = random.choice(fall_colors)
        draw_oval(canvas, bottom_row_lower_x + (x * offset), bottom_row_lower_y, bottom_row_upper_x + (x * offset), bottom_row_upper_y, outline=color, fill=color)
  
    # Diagonal offset. Third row
    third_row_lower_x = bottom_row_lower_x - offset
    third_row_lower_y = bottom_row_lower_y - offset
    third_row_upper_x = bottom_row_upper_x - offset
    third_row_upper_y = bottom_row_upper_y - offset

    for x in range(6):
        color = random.choice(fall_colors)
        draw_oval(canvas, third_row_lower_x + (x * offset), third_row_lower_y, third_row_upper_x + (x * offset), third_row_upper_y, outline=color, fill=color)
  
    # Diagonal offset. Fourth row. Starts to move inward. Note offsets
    fourth_row_lower_x = third_row_lower_x + offset
    fourth_row_lower_y = third_row_lower_y - offset
    fourth_row_upper_x = third_row_upper_x + offset
    fourth_row_upper_y = third_row_upper_y - offset

    for x in range(4):
        color = random.choice(fall_colors)
        draw_oval(canvas, fourth_row_lower_x + (x * offset), fourth_row_lower_y, fourth_row_upper_x + (x * offset), fourth_row_upper_y, outline=color, fill=color)
  
    # Diagonal offset. Fifth row. Starts to move inward. Note offsets
    fifth_row_lower_x = fourth_row_lower_x + offset
    fifth_row_lower_y = fourth_row_lower_y - offset
    fifth_row_upper_x = fourth_row_upper_x + offset
    fifth_row_upper_y = fourth_row_upper_y - offset

    for x in range(2):
        color = random.choice(fall_colors)
        draw_oval(canvas, fifth_row_lower_x + (x * offset), fifth_row_lower_y, fifth_row_upper_x + (x * offset), fifth_row_upper_y, outline=color, fill=color)
  
    trunk_upper_x = fifth_row_lower_x + offset
    trunk_upper_y = fifth_row_lower_y
    trunk_lower_x = trunk_upper_x + offset 
    trunk_lower_y = trunk_upper_y - (2 * offset)
    
    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_upper_x, trunk_upper_y,
            trunk_lower_x, trunk_lower_y, outline="brown", fill="brown")

    draw_rectangle

# Call the main function so that
# this program will start executing.
main()
