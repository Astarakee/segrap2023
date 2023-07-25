import os
import re

ch_order = re.compile('([0-9]+)')

def natural_sort_key(my_string):
    """
    sorting all the strings with a fixed rule

    Parameters
    ----------
    s : string
        A string to be sorted.

    Returns
    -------
    list
        sorted alphabetically and numerically.

    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(ch_order, my_string)]


def path_contents(absolute_path):
    """
    return names of all files and folders 

    Parameters
    ----------
    absolute_path : string
        absolute path of a directory.

    Returns
    -------
    filenames : list
        sorted names of all files/folders with the main dir.

    """
    filenames = os.listdir(absolute_path)
    filenames.sort(key=natural_sort_key)
    return filenames


def path_contents_pattern(absolute_path, pattern='.nii.gz'):
    """
    return names of certain files/folders that contain
    a certain pattern in their filenames. e.g, only nifti files.

    Parameters
    ----------
    absolute_path : string
        absolute path of a directory.
    pattern : string
        specify the file names or extension.

    Returns
    -------
    filenames : list
        sorted names of certain files/folders with the main dir..

    """
    filenames = path_contents(absolute_path)
    filenames = [x for x in filenames if pattern in x]
    filenames.sort(key=natural_sort_key)
    return filenames


def create_path(absolute_path):
    '''
    create an empty folder

    Parameters
    ----------
    absolute_path : string
        absolute path of the directory to be created.

    Returns
    -------
    None.

    '''
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
    else:
        pass
    return None
