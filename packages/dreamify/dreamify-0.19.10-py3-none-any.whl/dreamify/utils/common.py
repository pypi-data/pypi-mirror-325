import IPython.display as display
import numpy as np
import PIL.Image


def show(img):
    """Display an image."""
    img = np.array(img)
    img = np.squeeze(img)
    display.display(PIL.Image.fromarray(img))
