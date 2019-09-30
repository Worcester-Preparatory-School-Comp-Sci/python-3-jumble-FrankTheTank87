#Frank Carter 9/30
import random

x = 1
wordList = ["somebody", "cucumber", "maelstrom", "potato", "hippopotamus", "world", "yellow", "gonna", "A$AP Rocky", "Saylar", "aint", "ribbon", "sharpest", "tools", "inside", "sweater", "shed", "roll"]
#picks a random word from the list
def randWord(wordList):
    chosen = random.choice(wordList)
    word = list(chosen)
    random.shuffle(word)
    x = ''.join(word)
    return x
#allows the user to guess the word
def guess():
    guess = input("What is your guess?")
    if guess == randWord(wordList):
        print("Correct!")
        x == 1
        return x
    else:
        print("Wrong, try again")
        x = 0
        return 0
#if the user correctly guesses the word, the function breaks, if not, they are given another random word
while x == 1:
    if randWord(wordList) in wordList:
        chosen = random.choice(wordList)
        word = list(chosen)
        random.shuffle(word)
        x = ''.join(word)
    print("The scrambled word is "+randWord(wordList))
    guess = input("What is your guess?")
    if guess in wordList:
        print("Correct!")
        break
    else:
        print("Wrong, try again")
