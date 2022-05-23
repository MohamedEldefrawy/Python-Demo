import math


def get_distance_between_two_points(x2, x1, y2, y1):
    return float(math.sqrt(math.pow(x2 - x1) + math.pow(y2 - y1)))


def reduce_list(a_list):
    print()
    result = []
    for i in set(a_list):
        result.append(i)
    return result


def split_string(first_str, second_str):
    temp = first_str
    first_str_front = temp[:math.ceil(len(temp) / 2)]
    temp = first_str
    first_str_back = temp[len(first_str_front):]
    temp = second_str
    second_str_front = temp[:math.ceil(len(temp) / 2)]
    temp = second_str
    second_str_back = temp[len(second_str_front) - 1:]
    return first_str_front + second_str_front + first_str_back + second_str_back


def get_count_of_words_in_file():
    file_name = input("Please Enter the file path\n")
    with open(file_name, "r") as f:
        data = f.read()
        words = data.split()

        words_dictionary = {}
        for word in words:
            if word in words_dictionary.keys():
                words_dictionary[str(word)] += 1
            else:
                words_dictionary[str(word)] = 1
        return words_dictionary


def create_most_used_words_in_file():
    with open('./popular_words.txt', 'w+') as f:
        count_of_numbers = get_count_of_words_in_file()
        i = 0
        for key in count_of_numbers.keys():
            f.write(key + "\n")
            i += 1
            if i == 20:
                break;


def remove_vowels(text):
    result = ""
    for letter in list(text):
        if letter not in ["a", "e", "i", "o", "u"]:
            result += letter
    print(result)


def get_char_occurs_number(text, target):
    index = 0
    indexes = []
    for letter in list(text):
        if letter == target:
            indexes.append(index)

        index += 1
    return indexes


result = get_char_occurs_number("ohello", "o")
print(result)
