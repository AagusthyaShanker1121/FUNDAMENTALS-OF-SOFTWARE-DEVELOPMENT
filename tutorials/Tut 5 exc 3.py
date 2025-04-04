def get_sentence():
    inpt = input("Enter a sentence from keyboard: ")
    return inpt

def count_vowels(inpt):
    curr_vowels = 0
    for i in range(len(inpt)):
        if inpt[i] in ['a', 'e', 'o', 'i', 'u']:
            curr_vowels += 1
    return curr_vowels

def show(curr_vowels):
    print(f"Calculating number of vowels in \n {inpt} \n Vowels: {curr_vowels}")

inpt = get_sentence()
while not '*' in inpt:
    curr_vowels = count_vowels(inpt)
    show(curr_vowels)
    inpt = get_sentence()

