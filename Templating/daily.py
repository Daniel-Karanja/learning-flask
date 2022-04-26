


def get_all_to_do():
    return f"<ul>{to_to_do()}</ul>"

def to_to_do():
    li=""
    # for key in toDo:
    #     li=li+f"<li><h1>On:<b>{key}</b> we {toDo[key]}</h1></li>"
    for key in toDo:
        href=f"http://127.0.0.1:5000/day/{key}"
        li=li+f"<a href={href}><li><h1 >On:<b>{key}</b> we {toDo[key]}</h1></li></a>"
    return li

def get_the_to_do(key):
    return f"<h1>On This Day {key}</h1><h2>{toDo[key]}</h2>"


# print(get_all_to_do())
# print("To Do Turn")
# print(to_to_do())