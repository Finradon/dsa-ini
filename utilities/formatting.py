
def roll_tuple_to_string(res_tuple: tuple) ->str:
    res = res_tuple[0]
    suc = res_tuple[1]

    if suc:
        suc_str = ":white_check_mark:"
        if len(res_tuple) == 3:
            tp = f"TP: {res_tuple[2]}"
        else:
            tp = ""
    else: 
        suc_str = ":x:"
        tp = ""

    return f'{suc_str}:{res} ' + tp
