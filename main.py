# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

 

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        print('the two string is an anagram')
        return True
    else:
        print('the two string is not an anagram')
word = input("your first string:")
anagram = input("your seond number") 
find_anagram(word,anagram)

