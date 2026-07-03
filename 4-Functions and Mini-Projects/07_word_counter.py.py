#“Write a program that counts the number of words in a sentence.”

def count_words(sentence):
    words = sentence.split()
    return len(words)

text = "I love python programming"

print("Number of words in the sentence: ", count_words(text))