import json

def check(tree, count_dict):
    if len(tree) == 3:
        check(tree[1], count_dict)
        check(tree[2], count_dict)
    else:
        if tree[1] in count_dict:
            count_dict[tree[1]] += 1
        else:
            count_dict[tree[1]] = 1

def gen(tree, count_dict):
    if len(tree) == 3:
        left = gen(tree[1], count_dict)
        right = gen(tree[2], count_dict)
        return [tree[0], left, right]
    else:
        if count_dict[tree[1]] < 5:
            return [tree[0], "_RARE_"]
        else:
            return tree

if __name__ == "__main__":
    with open("parse_train.dat", "r") as old_train:
        trees = [x.rstrip("\n") for x in old_train.readlines()]

    count_dict = {}
    for tree in trees:
        tree_loaded = json.loads(tree)
        check(tree_loaded, count_dict)
    print len(count_dict)

    with open("parse_train.dat.part1", "w") as new_train:
        for tree in trees:
            tree_loaded = json.loads(tree)
            tree_gen = gen(tree_loaded, count_dict)
            tree_gen_str = json.dumps(tree_gen)
            new_train.write(tree_gen_str + "\n")

