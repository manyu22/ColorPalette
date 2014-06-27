# Color Palette

Python script to generate color palette image from given image. Support average color detection as well as precise color detection in the inputted grid size.

Visit my related [blog post](http://iabhimanyu.wordpress.com/2012/03/26/image-color-palette-in-python/) for more info.

## Dependencies
Python Image Library

```
PIL-1.1.7
```

## Usage

```
$ python color_palette.py
```

Interactively ask for Grid side and method user wants to generate the palette image.

## Example
Input images to be stored in `input` folder kept in the same directory from where user wants to run the script.
Output will be stored in two folder named `color_average` and `color_palette` depending upon the option selected.

```
$ python color_palette.py
enter size of each grid  5
enter the method
1 for average 
2 for precise
1
```

