import random
import sys

import OpenGL.GL as gl
import glfw

def frand():
    x = random.random()
    if random.randint(0, 1) == 1:
        x *= -1
    return x

# Returns a corner that's not diagonally opposite
def choose_corner(prev_corner):
    corners = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    available_corners = [c for c in corners if c != (-prev_corner[0], -prev_corner[1])]
    return random.choice(available_corners)

def draw_dot_plot(num_points):
    gl.glPointSize(2.0)
    gl.glColor3f(0, 0, 0)
    gl.glBegin(gl.GL_POINTS)

    corners = [(1.0, 1.0), (-1.0, 1.0), (-1.0, -1.0), (1.0, -1.0)]
    c0 = random.randint(0, 3)
    corner0 = (corners[c0][0], corners[c0][1])
    p0 = (frand(), frand())
    prev_corner = corner0


    for i in range(num_points):
        # Pick a random corner
        corner = choose_corner(prev_corner)
        pi = ((p0[0] + corner[0]) / 2, (p0[1] + corner[1]) / 2)

        gl.glVertex2f(*pi)
        p0 = pi
        
        
        # Update prev_corner
        prev_corner = corner


    gl.glEnd()

def main():
    num_points = int(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    print(num_points, width, height)
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(width, height, "Dot Plot", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    gl.glOrtho(-1.1, 1.1, -1.1, 1.1, -1.0, 1.0)
    gl.glClearColor(1.0, 1.0, 1.0, 0.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    draw_dot_plot(num_points)
    glfw.swap_buffers(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

    glfw.terminate()

if __name__ == '__main__':
    main()
