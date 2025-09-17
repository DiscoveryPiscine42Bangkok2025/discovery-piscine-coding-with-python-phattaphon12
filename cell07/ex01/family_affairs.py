def find_the_redheads(dic):
    redheads = filter(lambda item: item[1] == "red", dic.items())
    return list(map(lambda item: item[0], redheads))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))