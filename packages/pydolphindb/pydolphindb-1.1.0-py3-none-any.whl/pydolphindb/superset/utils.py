import pandas as pd
import dolphindb.settings as keys
import numpy as np


def mutator_temporary_pandas(data: pd.Timestamp, elem_type: int):
    if data is None:
        return None
    if elem_type in [keys.DT_NANOTIME, keys.DT_NANOTIMESTAMP]:
        return data
    if elem_type in [keys.DT_TIME, keys.DT_MINUTE, keys.DT_SECOND]:
        return data.to_pydatetime().time()
    return data.to_pydatetime()


def mutator_temporary_numpy(data: np.datetime64, elem_type: int):
    if data is None:
        return None
    if data.dtype == np.dtype("datetime64[ns]"):
        return pd.Timestamp(data)
    if elem_type in [keys.DT_TIME, keys.DT_MINUTE, keys.DT_SECOND]:
        return data.tolist().time()
    return data.tolist()


def mutator_array(data: list, elem_type: int):
    if keys.getCategory(elem_type) != keys.DATA_CATEGORY.TEMPORAL:
        return data
    return [mutator_temporary_numpy(x, elem_type) for x in data]
