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

def get_all_words_tags(filename):
    all_words = []
    all_tags = []
    rares = ["_RARE_", "_CAPITAL_", "_LAST_", "_DIGIT_"]

    with open(filename, "r") as train:
            lines = [x.rstrip("\n").split() for x in train.readlines()]
            for line in lines:
                if len(line) == 0:
                    pass
                else:
                    word = line[0]
                    tag = line[1]
                    if word not in all_words and word not in rares:
                        all_words.append(word)
                    if tag not in all_tags:
                        all_tags.append(tag)

    return all_words, all_tags
