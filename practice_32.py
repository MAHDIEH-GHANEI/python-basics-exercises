#“Write a program that counts the number of words in a sentence.”

def count_words(sentence):
    words = sentence.split()  #convert to list
    return len(words) #return len(sentence.split())

string = "I love python programming"

print("Number of words in the sentence: ", count_words(string))