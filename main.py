# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#def find_anagram(word, anagram):
#    # [assignment] Add your code here

#    return True

def find_anagram():
    first = input("What is the first word: ")
    second = input("What is the second word: ")

    first = first.lower()
    second = second.lower()

    if(sorted(first) == sorted(second)):
        return True
    else:
        return False
print(find_anagram())