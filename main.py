import pandas


def generate_phonetic():
    dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
    word = input("Type word :").upper()
    try:
        result_list = [dict[letter] for letter in word]
    except KeyError:
        print(f"invalid word : {word}. Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result_list)

if __name__ == "__main__":
    generate_phonetic()
