def object_with_id_exists(objects: list, target_id: str, id_key: str) -> bool:
    if len(objects) == 0:
        return False
    return any(obj for obj in objects if int(obj[id_key]) == int(target_id))


def format_list(json_list: list, property_order: list) -> list:
    reordered_list = []
    for obj in json_list:
        reordered_obj = {key: obj[key] for key in property_order if key in obj}
        reordered_list.append([reordered_obj[key] for key in property_order])
    return reordered_list


def truncate_string(input_string: str, length: int) -> str:
    return input_string[:length]
