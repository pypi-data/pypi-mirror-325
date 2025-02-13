import IPython.display as display
import numpy as np
import PIL.Image
import tensorflow as tf


def show(img):
    """Display an image."""
    display.display(PIL.Image.fromarray(np.array(img)))


def deprocess(img):
    """Normalize image for display."""
    img = tf.squeeze(img)
    img = 255 * (img + 1.0) / 2.0
    return tf.cast(img, tf.uint8)
