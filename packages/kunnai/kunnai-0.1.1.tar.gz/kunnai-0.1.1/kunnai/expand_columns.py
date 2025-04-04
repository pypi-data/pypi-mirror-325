import pandas as pd


def expand_dict_columns(data: pd.DataFrame) -> pd.DataFrame:
    dict_columns = [
        x for x in data.columns if all(data[x].apply(lambda y: isinstance(y, dict)))
    ]
    columns_list = [data.drop(columns=dict_columns).copy()]
    for dict_column in dict_columns:
        exploded_column = pd.json_normalize(data[dict_column])
        columns_list.append(exploded_column.copy())
    return pd.concat(columns_list, axis=1)


def expand_list_columns(data: pd.DataFrame) -> pd.DataFrame:
    list_columns = [
        x for x in data.columns if all(data[x].apply(lambda y: isinstance(y, list)))
    ]
    return data.explode(list_columns)
