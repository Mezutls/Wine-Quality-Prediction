import base64
from io import BytesIO
import matplotlib.pyplot as plt

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def plot_to_base64(fig):
    """
    Converts a Matplotlib figure to a base64-encoded image.

    Parameters:
    - fig: Matplotlib figure object

    Returns:
    - str: base64-encoded image data URI
    """
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()
    buffer.close()
    base64_encoded = base64.b64encode(image_data).decode('utf-8')
    return f'data:image/png;base64,{base64_encoded}'
