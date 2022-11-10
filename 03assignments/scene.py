# Import the functions from the Draw 2-D library
# so that they can be used in this program.
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
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)


    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="gray35")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")





    #This is a pine tree
    tree_center_x = 180
    tree_bottom = 130
    tree_height = 270
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 570
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    #This is another pine tree
    tree_center_x = 690
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

# Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")




    #draw_picket
    height = 150
    width = 500
    draw_pickets(canvas, width, height, 50)


def draw_pickets(canvas,width,height, interval):
    # height_x = 40
    #for vertical lines
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, width=30, fill="brown4")
        # draw_line(canvas, x, 0, x, height_x, width=1, fill="green")
    # height_x = 40
    #for horizontal lines
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, width=30, fill="brown4")
        # draw_line(canvas, x, 0, x, height_x, width=1, fill="green")





 #draw a cloud
    center_x = 200
    bottom = 400
    height = 750
    draw_cloud(canvas, center_x, bottom, height)
    center_x = 230
    bottom = 400
    height = 850
    draw_cloud(canvas, center_x, bottom, height)
    center_x = 270
    bottom = 400
    height = 750
    draw_cloud(canvas, center_x, bottom, height)

 #Draw another cloud
    center_x = 650
    bottom = 380
    height = 750
    draw_cloud(canvas, center_x, bottom, height)
    center_x = 680
    bottom = 380
    height = 850
    draw_cloud(canvas, center_x, bottom, height)
    center_x = 720
    bottom = 380
    height = 750
    draw_cloud(canvas, center_x, bottom, height)


def draw_cloud(canvas, center_x, bottom, height):
    """This is for clouds"""
    width = height / 7
    height = height / 10
    cloud_left = center_x - width / 3
    cloud_right = center_x + width / 2
    cloud_top = bottom + height
    draw_oval(canvas, cloud_left, cloud_top, cloud_right, bottom, outline = "gray19", width = 1, fill = "gray19")





    #draw sun
    center_x = 100
    bottom = 400
    height = 850
    draw_sun(canvas, center_x, bottom, height)

def draw_sun(canvas, center_x, bottom, height):
    """This is the sun"""
    width = height / 8
    height = height / 10
    cloud_left = center_x - width / 3
    cloud_right = center_x + width / 2
    cloud_top = bottom + height
    draw_oval(canvas, cloud_left, cloud_top, cloud_right, bottom, outline = "maroon", width = 1, fill = "orange")
# Call the main function so that
# this program will start executing.

main()