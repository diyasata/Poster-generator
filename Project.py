import numpy as np
from ColabTurtlePlus.Turtle import *
from TileFunctions import tile_functions
from PalleteOptions import palette_options
def generate_poster():

    title_text = input("Enter a title for your poster: ")

    nrows = int(input("Grid height: "))
    while nrows < 3 or nrows > 8:
        print("Should be between 3 and 8.")
        nrows = int(input("Grid height: "))

    ncols = int(input("Grid width: "))
    while ncols < 3 or ncols > 8:
        print("Should be between 3 and 8.")
        ncols = int(input("Grid width: "))

    palette_names = list(palette_options.keys()) + ["random"]

    p_name = input("Enter the name of the color palette you wish to use: ").lower()

    while p_name not in palette_names:
        print(f"Invalid palette name. The valid names are {palette_names}.")
        p_name = input("Enter the name of the color palette you wish to use: ").lower()

    print(f"You have selected the {p_name} palette.")

    if p_name == "random":
        print("Now generating a random color palette...")
        palette = {}

        for key in ["bg", "primary", "secondary", "accent"]:
            r = np.random.randint(256)
            g = np.random.randint(256)
            b = np.random.randint(256)
            palette[key] = (r, g, b)

    else:
        palette = palette_options[p_name]

    screen_width = 1000
    screen_height = 500

    horizontal_spacing = 20
    vertical_spacing_above = 20
    vertical_spacing_below = 180

    size_horiz = (screen_width - horizontal_spacing * 2) / ncols
    size_vert = (screen_height - vertical_spacing_above - vertical_spacing_below) / nrows
    size = min(size_horiz, size_vert)

    # Screen Setup
    clearscreen()
    setup(screen_width, screen_height)
    t = Turtle()
    t.speed(0)

    y_offset = screen_height / 2 - 20 - size / 2
    x_offset = size * (ncols - 1) / 2

    for row in range(nrows):
        y = y_offset - size * row

        for col in range(ncols):
            x = x_offset - size * col

            # Randomly choose which person's tile to draw
            F = tile_functions[np.random.randint(len(tile_functions))]

            if row == 0:
                if col == 0:
                    tile_type = "corner"
                    rotation = 0
                elif col == ncols - 1:
                    tile_type = "corner"
                    rotation = 90
                else:
                    tile_type = "border"
                    rotation = np.random.randint(2) * 180

            elif row == nrows - 1:
                if col == 0:
                    tile_type = "corner"
                    rotation = 270
                elif col == ncols - 1:
                    tile_type = "corner"
                    rotation = 180
                else:
                    tile_type = "border"
                    rotation = np.random.randint(2) * 180

            else:
                if col == 0 or col == ncols - 1:
                    tile_type = "border"
                    rotation = 90 + np.random.randint(2) * 180
                else:
                    tile_type = "center"
                    rotation = np.random.randint(4) * 90

            F(t, x, y, size, rotation, palette, tile_type)

    # Write the title and credits
    t.penup()
    t.jumpto(0, -screen_height / 2 + vertical_spacing_below - 30)
    t.write(title_text, align="center", font=(20, "Arial", "bold"))

    t.setheading(270)
    t.forward(30)
    t.write("By Adam, Winni, and Diya",
            align="center",
            font=(20, "Arial", "bold"))

    # Draw the color palette colors
    t.penup()
    t.jumpto(-145, -200)

    for v in palette.values():
        t.color(v, v)
        t.setheading(90)
        t.pendown()
        t.begin_fill()

        t.forward(40)
        t.right(120)
        t.forward(40)
        t.right(120)
        t.forward(40)

        t.end_fill()
        t.penup()

        t.setheading(270)
        t.forward(15)
        t.write(v, align="Right")

        t.setheading(90)
        t.forward(15)
        t.setheading(0)
        t.forward(90)

    t.hideturtle()
    t.done()
    
    saveSVG("/content/poster.svg")
