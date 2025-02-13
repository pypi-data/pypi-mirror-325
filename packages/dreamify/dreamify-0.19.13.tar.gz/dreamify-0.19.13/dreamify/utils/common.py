import PIL.Image
import IPython.display as display

def show(img):
    """Display an image."""
    display.display(PIL.Image.fromarray(np.array(img)))