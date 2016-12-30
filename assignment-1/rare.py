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
    with open("gene.train.part1", "w") as new_train:
        lines = [x.rstrip("\n").split() for x in train.readlines()]
        for line in lines:
            if len(line) == 0:
                new_train.write("\n")
            else:
                if frequency_dict[line[0]] < 5:
                    new_train.write("_RARE_ " + line[1] + "\n")
                else:
                    new_train.write(line[0] + " " + line[1] + "\n")
