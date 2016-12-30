def convert(filename):
    """
    Converts counts in file to a Python dictionary
    """
    count_dict = dict()

    with open(filename, "r") as counts:
        counts_list = [x.rstrip("\n").split() for x in counts.readlines()]
        for count in counts_list:
            if count[1] == "WORDTAG":
                count_dict[(count[2], count[3])] = count[0]
            elif count[1] == "1-GRAM":
                count_dict[(count[2])] = count[0]
            elif count[1] == "2-GRAM":
                count_dict[(count[2], count[3])] = count[0]
            else:
                count_dict[(count[2], count[3], count[4])] = count[0]

    return count_dict
