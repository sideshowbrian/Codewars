"""
The goal of this exercise is to convert a string to a new string where each character 
in the new string is "(" if that character appears only once in the original string, 
or ")" if that character appears more than once in the original string. Ignore 
capitalization when determining if a character is a duplicate.

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""
test1 = "din"
test2 = "recede"
test3 = "Success"
test4 = "TbRkc IF@x kuaGQ buR G)P"

def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    for char in word:
        if word.count(char) > 1:
            new_word = new_word + ")"
            print(char)
        else:
            new_word = new_word + "("
    print (new_word)

duplicate_encode(test4)
print('()))()(((()))()())))))((')
