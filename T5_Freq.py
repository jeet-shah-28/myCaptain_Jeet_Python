import operator

def most_frequent(word):
    word = word.lower()
    freq = dict()
    for letter in word:
        freq[letter] = 1 if letter not in freq else freq[letter] + 1
    freq = dict(sorted(freq.items(), key=operator.itemgetter(1), reverse=True))
    for key,value in freq.items():
        print(key,"=",value,sep="",end=" ")

def main():
    most_frequent(input("Enter a string : "))

if __name__ == '__main__':
    main()