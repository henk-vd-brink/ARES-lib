import json


def float_reformatter(input_dict: dict):
    output_dict = dict()

    for key, value in input_dict.items():
        if isinstance(value, float):
            value = round(value, 3)

        elif isinstance(value, list):
            value = [round(item, 3) for item in value]

        elif isinstance(value, dict):
            value = float_reformatter(value)

        else:
            pass

        output_dict[key] = value
    return output_dict


def message_reformatter(input_dict: dict):
    output_dict = float_reformatter(input_dict=input_dict)
    return json.dumps(output_dict)