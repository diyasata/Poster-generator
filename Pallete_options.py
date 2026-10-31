palette_options = {} 

# Color palette for person 1 here
adam_palette = {
        "bg": (20, 5, 80),
        "primary": (10, 50, 180),
        "secondary": (90, 120, 50),
        "accent": (20, 106, 40)
    }

# Add this line at the end
palette_options["deep ocean palette"] = adam_palette
# Add this line at the end
# palette_options["my palette's name"] = my_palette_dictionary

# Color palette for person 2 here
diya_palette = {
        "bg": (253, 253, 207),
        "primary": (51, 153, 255),
        "secondary": (0, 102, 204),
        "accent": (255, 128, 0)
    }

# Add this line at the end
palette_options["bright"] = diya_palette

# Color palette for person 3 here

winni_palette = {
        "bg": (97, 161, 158),
        "primary": (86, 86, 99),
        "secondary": (166, 81, 88),
        "accent": (255, 189, 0)
    }

# Add this line at the end
palette_options["muted"] = winni_palette

palette_names = list(palette_options)
palette_names.append("random")
print(f"The available color palettes are: {palette_names}") 