from contents import recipes


def deepcopy(original_dict: dict) -> dict:
    """

    :param original_dict:
    :return:
    """
    deep_dict = {}
    for key, value in original_dict.items():
        deep_dict_value = value.copy()
        deep_dict[key] = deep_dict_value
    return deep_dict



recipes_copy = deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"]= 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
