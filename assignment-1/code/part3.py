from part1 import emission_prob
from common import convert, get_all_words_tags

def trigram_prob(tag1, tag2, tag3, count_dict):
    if (tag1, tag2, tag3) in count_dict:
        trigram_count = float(count_dict[(tag1, tag2, tag3)])
        bigram_count = int(count_dict[(tag1, tag2)])
        prob = trigram_count / bigram_count
    else:
        prob = 0

    return prob

def S(position):
    if position < 1:
        return ["*"]
    else:
        return all_tags

def get_emission_prob(word, tag, count_dict):
    if word in all_words:
        prob = emission_prob(word, tag, count_dict)
    else:
        if word.isupper():
            prob = emission_prob("_CAPITAL_", tag, count_dict)
        elif any(char.isdigit() for char in word):
            prob = emission_prob("_DIGIT_", tag, count_dict)
        elif word[-1].isupper():
            prob = emission_prob("_LAST_", tag, count_dict)
        else:
            prob = emission_prob("_RARE_", tag, count_dict)

    return prob

def pi(k, tag1, tag2, dp_dict):
    if (k, tag1, tag2) in dp_dict:
        return dp_dict[(k, tag1, tag2)]
    else:
        max_prob = -1
        max_tag0 = ""
        for tag0 in S(k-2):
            prob = pi(k-1, tag0, tag1, dp_dict) * trigram_prob(tag0, tag1, tag2, count_dict) * get_emission_prob(sentence[k-1], tag2, count_dict)
            if prob > max_prob:
                max_prob = prob
                max_tag0 = tag0
        dp_dict[(k, tag1, tag2)] = max_prob
        back_pointer[(k, tag1, tag2)] = max_tag0
        return max_prob

def viterbi(sentence_len, dp_dict, all_tags):
    for k in range(1, sentence_len + 1):
        for tag1 in S(k-1):
            for tag2 in S(k):
                pi(k, tag1, tag2, dp_dict)

def gen_dict():
    dp_dict = {}
    dp_dict[(0, "*", "*")] = 1
    back_pointer = {}

    return dp_dict, back_pointer

def find_sequence(sentence_len, dp_dict, back_pointer):
    # for k, v in back_pointer.iteritems():
        # print k, v
    max_prob = -1
    max_tag1 = ""
    max_tag2 = ""
    sequence = []

    for tag1 in all_tags:
        for tag2 in all_tags:
            if dp_dict[(sentence_len, tag1, tag2)] > max_prob:
                max_prob = dp_dict[(sentence_len, tag1, tag2)]
                max_tag1 = tag1
                max_tag2 = tag2
    sequence.append(max_tag2)
    sequence.append(max_tag1)
    cur_tag1 = max_tag1
    cur_tag2 = max_tag2

    for k in range(sentence_len, 2, -1):
        tag0 = back_pointer[(k, cur_tag1, cur_tag2)]
        sequence.append(tag0)
        cur_tag2 = cur_tag1
        cur_tag1 = tag0

    sequence.reverse()

    return sequence


if __name__ == "__main__":
    count_dict = convert("gene.counts.part3")

    all_words, all_tags = get_all_words_tags("gene.train.part3")

    with open("gene.dev", "r") as dev:
        with open("gene_dev.p3.out", "w") as output:
            words = [x.rstrip("\n") for x in dev.readlines()]
            sentence = []
            for word in words:
                if word != "":
                    sentence.append(word)
                else:
                    dp_dict, back_pointer = gen_dict()
                    viterbi(len(sentence), dp_dict, all_tags)
                    sequence = find_sequence(len(sentence), dp_dict, back_pointer)
                    for i in range(len(sentence)):
                        output.write(sentence[i] + " " + sequence[i] + "\n")
                    output.write("\n")
                    sentence = []

