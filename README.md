# OpenGL-DotPlot

This exercise involves creating an OpenGL program to draw a dot plot using a simple algorithm. The algorithm randomly places points within a square defined by opposite corners (𝑥𝑚𝑖𝑛, 𝑦𝑚𝑖𝑛) and (𝑥𝑚𝑎𝑥, 𝑦𝑚𝑎𝑥). The points are drawn using immediate mode and displayed on the screen.

## Instructions

1. Clone this repository or download the necessary files.
2. Make sure you have the required libraries installed (OpenGL, GLFW).
3. Run the provided Python script with the required command line arguments to visualize the dot plot.

## How to Run

1. Install the required libraries using the following command (if you haven't already):

```bash
pip install glfw PyOpenGL
```

2. Run the script with command line arguments:

```bash
python dot_plot.py N screen_width screen_height
```

Replace `N`, `screen_width`, and `screen_height` with the desired values. The program will generate 𝑁 points within the square, and the resulting dot plot will be displayed in a window with the specified width and height.

## Specifications

- Viewing Volume: (left, right, bottom, top) = (-1.1, 1.1, -1.1, 1.1)
- Background Color: White
- Dot Color: Black
- Square Corners: 𝑥𝑚𝑖𝑛 = 𝑦𝑚𝑖𝑛 = -1, 𝑥𝑚𝑎𝑥 = 𝑦𝑚𝑎𝑥 = 1
- Point Size: 2.0

## Dot Plot Drawing Algorithm

1. Define the opposite corners of a square using (𝑥𝑚𝑖𝑛, 𝑦𝑚𝑖𝑛) and (𝑥𝑚𝑎𝑥, 𝑦𝑚𝑎𝑥).
2. Choose a random corner of the square 𝑐0 (remember squares have four possible corners).
3. Choose a random point 𝑝0 (𝑥, 𝑦) such that 𝑥𝑚𝑖𝑛 < 𝑥 < 𝑥𝑚𝑎𝑥 and 𝑦𝑚𝑖𝑛 < 𝑦 < 𝑦𝑚𝑎𝑥.
4. For each iteration from 1 to 𝑁:
   - (a) Choose a random corner 𝑐𝑖 of the square, which is not diagonally opposite to 𝑐𝑖−1.
   - (b) Let 𝑝𝑖 be the point halfway between 𝑝𝑖−1 and 𝑐𝑖.
   - (c) Draw a point at 𝑝𝑖.
