import pandas as pd

def na_padding(x, max_len, pad_offset = 0, na_value = "NA"):
    """
    Pads a list with NA's to achive a target length.
    """

    if len(x) < max_len:
        x = x[: -pad_offset] + (["NA" for i in range(max_len - len(x))]) + x[-pad_offset:]
        return x
    else:
        return x

def uneven_list_to_df(l, col_names = None, max_len = None, na_pad_offset = 0, na_value = "NA"):
    """
    Converts an uneven list of lists to a pandas DataFrame 
    by padding each list item to be of same length.
    """
    
    # infer max_len if not provided
    if max_len is None:
        max_len = max(map(len, l))
    else:
        pass

    # Create default variable names if none provided
    if col_names is None:
        col_names = ["V" + str(i) for i in range(max_len)]
    else:
        pass

    # pad with NA's to make all list items the same length 
    x = list(map(lambda x: na_padding(x, max_len, na_pad_offset, na_value), l))

    # return dataframe
    return pd.DataFrame(x, columns = col_names)
    