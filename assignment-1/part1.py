from common import convert, get_all_words_tags

def emission_prob(word, tag, count_dict):
    count_tag = float(count_dict[tag])
    if (tag, word) in count_dict:
        count_tag_to_word = int(count_dict[(tag, word)])
    else:
        count_tag_to_word = 0
    em_prob = count_tag_to_word / count_tag

    return em_prob

def get_tag(word, count_dict, all_words, all_tags):
    max_prob = 0
    max_tag = ""
    if word in all_words:
        for tag in all_tags:
            prob = emission_prob(word, tag, count_dict)
            if prob > max_prob:
                max_prob = prob
                max_tag = tag
    else:
        # print "word unseen"
        for tag in all_tags:
            prob = emission_prob("_RARE_", tag, count_dict)
            # print "prob: ", str(prob), str(tag)
            if prob > max_prob:
                max_prob = prob
                max_tag = tag

    return max_tag

if __name__ == "__main__":
    count_dict = convert("gene.counts.part1")
    all_words, all_tags = get_all_words_tags("gene.train.part1")

    with open("gene.test", "r") as dev:
        with open("gene_test.p1.out", "w") as output:
            words = [x.rstrip("\n") for x in dev.readlines()]
            for word in words:
                if word == "":
                    output.write("\n")
                else:
                    tag = get_tag(word, count_dict, all_words, all_tags)
                    output.write(word + " " + tag + "\n")
