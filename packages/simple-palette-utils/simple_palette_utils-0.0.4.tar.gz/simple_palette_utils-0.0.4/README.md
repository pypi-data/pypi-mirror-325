# simple-palette-utils
Python3 library makes dealing with color palettes easy.

## Installation

From PyPI:

```bash
pip install simple_palette_utils
```

The latest code straight from the repository:

```bash
pip install git+https://github.com/waikato-datamining/simple-palette-utils.git
```

## Palettes

Available palettes:

* PALETTE_GRAYSCALE
* [PALETTE_X11](https://en.wikipedia.org/wiki/X11_color_names)
* PALETTE_LIGHT (from PALETTE_X11)
* PALETTE_DARK (from PALETTE_X11)
* [PALETTE_COLORBLIND8](http://mkweb.bcgsc.ca/colorblind/palettes/8.color.blindness.palette.txt)
* [PALETTE_COLORBLIND12](http://mkweb.bcgsc.ca/colorblind/palettes/12.color.blindness.palette.txt)
* [PALETTE_COLORBLIND15](http://mkweb.bcgsc.ca/colorblind/palettes/15.color.blindness.palette.txt)
* [PALETTE_COLORBLIND24](http://mkweb.bcgsc.ca/colorblind/palettes/24.color.blindness.palette.txt)

## Usage

Generating lists of color triplets:

```python
from simple_palette_utils import colors, x11_colors, COLOR_LIST_LIGHT

p = colors(COLOR_LIST_LIGHT)
print("colors/light\n", p)

p = x11_colors(no_light=True)
print("x11_colors/no light colors\n", p)
```

Generating palette lists:

```python
from simple_palette_utils import default_palette, grayscale_palette, PALETTE_X11, PALETTE_COLORBLIND8

p = default_palette()
print("default_palette\n", p)

p = default_palette(PALETTE_X11)
print("default_palette/X11\n", p)

p = default_palette(PALETTE_COLORBLIND8)
print("default_palette/colorblind8\n", p)

p = grayscale_palette(32)
print("grayscale_palette/32\n", p)
```

Generating palettes for indexed PNGs (get filled up to 256*3 values with grayscale colors):

```python
from simple_palette_utils import generate_palette_list, PALETTE_COLORBLIND8

p = generate_palette_list()
print("generate_palette_list\n", p)

p = generate_palette_list(PALETTE_COLORBLIND8)
print("generate_palette_list/colorblind8\n", p)

p = generate_palette_list("255,0,0,0,255,0,0,0,255")
print("generate_palette_list/custom RGB values\n", p)
```

Setting the palette for a Pillow Image:

```python
from PIL import Image
from simple_palette_utils import generate_palette_list, PALETTE_X11

img = Image.effect_noise((500, 500), 25)  # sigma=25
img.putpalette(generate_palette_list(PALETTE_X11))
img.save("demo.png")
```

Extending color lists/palettes:

```python
from simple_palette_utils import colors, generate_palette_list, add_palette, add_color_list

my_colors = [
"#C0C0C0",
"#808080",
"#000000",
"#FF0000",
"#800000",
"#FFFF00",
"#808000",
"#00FF00",
"#008000",
"#00FFFF",
"#008080",
"#0000FF",
"#000080",
"#FF00FF",
"#800080",
]
add_color_list("mycolors", my_colors)
add_palette("mycolors", my_colors)

p = colors("mycolors")
print("colors\n", p)

p = generate_palette_list("mycolors")
print("palette\n", p)
```

Overriding default PALETTE_GRAYSCALE with custom values:

```python
from simple_palette_utils import generate_palette_list, add_palette, PALETTE_GRAYSCALE

gray_colors = [
    "#000000",
    "#202020",
    "#404040",
    "#606060",
    "#808080",
    "#A0A0A0",
    "#C0C0C0",
    "#E0E0E0",
]
add_palette(PALETTE_GRAYSCALE, gray_colors)
p = generate_palette_list(PALETTE_GRAYSCALE)
print("custom gray\n", p)
```

Convert flat palette list into list of RGB triplets:

```python
from simple_palette_utils import generate_palette_list, PALETTE_GRAYSCALE, palette_list_to_triplets

p = generate_palette_list(PALETTE_GRAYSCALE)
print("flat list\n", p)
t = palette_list_to_triplets(p)
print("triplets\n", t)
```
