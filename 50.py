import csv
import random

HIRAGANA_FILE = "hiragana.csv"
KATAKANA_FILE = "katakana.csv"


def create_kana_dict():
    def create(kana_file):
        kana_dict = dict()
        with open(kana_file) as kana_csv:
            rows = csv.reader(kana_csv)
            for row in rows:
                kana_dict[row[1]] = row[0]
        return kana_dict

    hiragana_dict = create(HIRAGANA_FILE)
    katakana_dict = create(KATAKANA_FILE)
    return hiragana_dict, katakana_dict


def show_options():
    user_input = input("""[1]平假名/hiragana [2]片假名/katakana [Q/q]離開/quit
[3]印製平假名表/print hiragana table [4]印製片假名表/print katakana table
>>> """)
    return user_input


def make_test(kana_dict):
    def create_shuffle_sequence(upper):
        num_list = list(range(upper))
        random.shuffle(num_list)
        return num_list

    def error_report():
        if len(error_list) == 0:
            print("100% correct")
        else:
            print("error:")
            for i in error_list:
                roma = roma_list[i]
                print("{}: {}".format(kana_dict[roma], roma))

    kana_list = list(kana_dict.values())
    roma_list = list(kana_dict.keys())
    shuffle_sequence = create_shuffle_sequence(len(kana_dict))
    error_list = list()

    for i in shuffle_sequence:
        kana = kana_list[i]
        answer = input("{}: ".format(kana))

        if kana_dict.get(answer) == kana:
            print("correct")
        elif answer == 'q' or answer == 'Q':
            print("exit test")
            break
        else:
            error_list.append(i)
            print("Wrong! the answer is {}".format(roma_list[i]))
    error_report()


def print_table(kana_dict):
    i = 0
    for key in kana_dict:
        print("{}: {}".format(kana_dict[key], key), end='\t')
        i += 1
        if i == 5 or key == 'yo' or key == 'wo':
            i = 0
            print()
    print()


def main():
    hiragana_dict, katakana_dict = create_kana_dict()

    while True:
        user_input = show_options()
        if user_input == 'Q' or user_input == 'q':
            break
        elif user_input == '1':
            make_test(hiragana_dict)
        elif user_input == '2':
            make_test(katakana_dict)
        elif user_input == '3':
            print_table(hiragana_dict)
        elif user_input == '4':
            print_table(katakana_dict)


if __name__ == '__main__':
    main()
