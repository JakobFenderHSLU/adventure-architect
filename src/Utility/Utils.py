def check_attribute(attribute: str, dictionary: dict):
    if attribute not in dictionary or attribute is None:
        return False
    attribute_value = dictionary[attribute]
    if isinstance(attribute_value, str):
        return attribute_value.strip() != ""
    elif isinstance(attribute_value, list):
        return len(attribute_value) != 0
    elif isinstance(attribute_value, dict):
        return len(attribute_value) != 0
    else:
        return attribute_value is not None


def check_attributes(attributes: list, dictionary):
    for attribute in attributes:
        if not check_attribute(attribute, dictionary):
            return False
    return True
