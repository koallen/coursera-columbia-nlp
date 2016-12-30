with open("gene.counts", "r") as counts:
    frequency_dict = dict()

    count_list = [x.rstrip("\n").split() for x in counts.readlines()]
    for count in count_list:
        if count[1] == "WORDTAG":
            if count[3] in frequency_dict:
                frequency_dict[count[3]] += int(count[0])
            else:
                frequency_dict[count[3]] = int(count[0])

with open("gene.train", "r") as train:
    with open("gene.train.part3", "w") as new_train:
        lines = [x.rstrip("\n").split() for x in train.readlines()]
        for line in lines:
            if len(line) == 0:
                new_train.write("\n")
            else:
                if frequency_dict[line[0]] < 5:
                    if line[0].isupper():
                        new_train.write("_CAPITAL_ " + line[1] + "\n")
                    elif any(char.isdigit() for char in line[0]):
                        new_train.write("_DIGIT_ " + line[1] + "\n")
                    elif line[0][-1].isupper():
                        new_train.write("_LAST_ " + line[1] + "\n")
                    else:
                        new_train.write("_RARE_ " + line[1] + "\n")
                else:
                    new_train.write(line[0] + " " + line[1] + "\n")

