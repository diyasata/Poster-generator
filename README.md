# Poster Generator
An example of the generated poster is displayed here:

![Generated Poster](poster.svg)

## About the Project

This project is a generative poster creator made using Python and ColabTurtlePlus. It creates unique geometric posters using randomly selected tile designs, different grid sizes, and customizable color palettes.

Users can choose a title, grid dimensions, and a color palette. The program then generates a unique poster.

## The Interface

Users may provide input within the poster generator regarding the title of the poster, grid height, grid width, and the name of the color palette they wish to use. 

## How Does it Work?

Pallete_options.py contains all palettes and contains them into a list. Tilefunctions.py contains three different functions that draws an array of different types of border, center, and corner tiles. The python script project.py, pulls from Pallete_options.py and runs a singular function that uses one color palette and generates a grid comprised of random tiles from each tile function. The poster generation function first asks for the user's input on the poster title, grid height, grid width, and palette before configuring the poster with the aforementioned settings.

## Group Members

- Adam: Typography & Exhibition Curator 
- Winni: Coordinate & Grid Architect, Rules & Logic Director
- Diya: Interaction & Data Engineer 

## How to Run

The project can be run using Google Colab.

Copy and run the following code in a Colab notebook:

```python
!git clone https://github.com/diyasata/Poster-generator.git
%cd Poster-generator
!pip install -r requirements.txt

from Project import generate_poster

generate_poster()
```
Or click below to open an example notebook in Google Colab and generate your own poster!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1uPXAB8BiiwR5xlE9IJ9dD18557l9ywfz#scrollTo=SjDNdbyvcH3c)


## Project Files

- `project.py` – Main program that generates the poster.
- `PaletteOptions.py` – Contains the available color palettes.
- `TileFunctions.py` – Contains the functions used to draw the poster tiles.
- `requirements.txt` – Lists the required Python library.
