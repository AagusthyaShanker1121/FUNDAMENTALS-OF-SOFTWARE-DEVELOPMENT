# Develop the program Lab9Exercise1 (with Python) that as follows:
# • Read a string from user-input until *
# • Determine the vowel frequency in each string and store the result into a text file: vowels.txt
# vowels.txt data should be formatted as:
# <vowel> ---> <frequency>
# • After the loop is terminated, read and show the vowels.txt content
# Lab 9 – Lab9Exercise1

def get_input():
    x = input("Enter a string followed by a '*': ")
    return x.split("*")[0]

def count_vowels(x):
    vowels = {k: 0 for k in "aeiou"}
    for i in range(len(x)):
        if x[i] in vowels.keys():
            vowels[x[i]] += 1
    return vowels

def output_to_file(vowels):
    with open("file.txt", "w") as handler:
        for i in vowels.keys():
            handler.write(f"{i} ---> {vowels[i]}")
            handler.write(f"\n")

output_to_file(count_vowels(get_input()))
