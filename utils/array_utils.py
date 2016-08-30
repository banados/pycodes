import numpy as np

def get_ind(val, arr):
    '''
    get a value and an array.
    Returns the index of the closest element of the array to the value
    '''
    return min(range(len(arr)), key=lambda i: abs(arr[i] - val))
    

def between(a, vmin, vmax):
    """ Return a boolean array True where vmin <= a < vmax.
    Notes
    -----
    Careful of floating point issues when dealing with equalities.

    Taken from Neil Crighton's codes
    """
    a = np.asarray(a)
    c = a < vmax
    c &= a >= vmin
    return c


def lowercase_table_keywords(data):
    """
    Receives a Table or fits file with column names.
    They are all lowercased and the table is returned

    """

    for old_col, new_col in zip(data.colnames, np.char.lower(data.colnames)):
        data[old_col].name = 'tmpcol'
        data['tmpcol'].name = new_col

    return data