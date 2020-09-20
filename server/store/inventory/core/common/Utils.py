

_DATA_REPOSITORY = ""

def is_dict_empty(d: dict = {}):
    key_count = len(d.keys)
    return True if key_count > 0 else False

def is_arr_empty(a: list = []):
    return True if len(a) > 0 else False


def get_data_repository():
    if str(_DATA_REPOSITORY).strip() == "" :
        