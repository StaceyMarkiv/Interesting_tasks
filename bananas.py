from itertools import combinations


def bananas(s) -> set:
    word = "banana"
    if s.count("b") >= 1 and s.count("a") >= 3 and s.count("n") >= 2:
        if s == word:
            result = {s}
        else:
            addition = len(s) - len(word)
            index_variants = list(combinations(range(len(s)), addition))

            var_list = []
            for ind_var in index_variants:
                word_var = list(s)
                for el in ind_var:
                    word_var[el] = "-"
                var_list.append(word_var)

            result_list = []
            for var_word in var_list:
                test_res_word = "".join(var_word)
                new_test_word = test_res_word.replace("-", "")
                # Проверка, соответствует ли полученная комбинация букв без "-" слову "banana":
                if new_test_word == word:
                    count = 0
                    for i in range(len(s)):
                        # Проверка, находятся ли буквы в полученной комбинации на тех же местах, что и в исходной строке:
                        if test_res_word[i] != "-" and test_res_word[i] == s[i]:
                            count += 1
                    if count == len(word):
                        result_list.append(test_res_word)
            result = set(result_list)
    else:
        result = set()

    return result


if __name__ == "__main__":
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
