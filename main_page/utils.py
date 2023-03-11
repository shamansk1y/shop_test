import os
import uuid


def get_file_name(instance, filename):
    """
    Create a unique file name for an uploaded file.
    Args:
        instance: An instance of a class.
        filename (str): The original name of the uploaded file.
    Returns:
        str: A unique file name for the uploaded file.
    """
    ext = filename.strip().split('.')[-1]
    new_file_name = f'{uuid.uuid4()}.{ext}'
    return os.path.join(instance.__class__.__name__.lower(), new_file_name)