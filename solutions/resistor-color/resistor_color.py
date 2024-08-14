def color_code(color):
    color_list = colors()

    if color in color_list:
        return color_list.index(color)
    else:
        return None


def colors():
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
        ]