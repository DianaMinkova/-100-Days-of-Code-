from turtle import onscreenclick, mainloop

""" How can find the position states,
    we need to know what is the X and Y coordinate of this location."""


def get_mouse_click_coor(x, y):
    print(x, y)


onscreenclick(get_mouse_click_coor)  # Create EventListener with X and Y coordinate.

mainloop()  # Keep screen open to take coordinate.
