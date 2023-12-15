def clear_dict_from_none(dct: dict):
    return dict(filter(lambda item: item[1] is not None, dct.items()))
