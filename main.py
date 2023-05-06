import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data = pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic_word():
    word = input("Enter your word:").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except:
        print("Sorry only letter in the alphabet please!")
        phonetic_word()
    else:
        print(output_list)

phonetic_word()

