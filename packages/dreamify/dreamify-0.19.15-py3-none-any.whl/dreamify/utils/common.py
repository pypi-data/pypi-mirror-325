import IPython.display as display
import numpy as np
import PIL.Image


def show(img):
    """Display an image."""
    display.display(PIL.Image.fromarray(np.array(img)))
