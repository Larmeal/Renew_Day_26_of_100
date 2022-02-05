import pandas

data_nato = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
dict_word = {row.letter:row.code for (index, row) in data_nato.iterrows()}

word = input("Enter word: ").upper()
split_word = [n for n in word]

alphabit = [dict_word[n] for n in split_word]

print(alphabit)