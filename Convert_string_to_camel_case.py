"""
Complete the method/function so that it converts dash/underscore delimited words into camel 
casing. The first word within the output should be capitalized only if the original word was 
capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""
test1 = "the-stealth-warrior"
test2 = "The_Stealth_Warrior"

import re

def to_camel_case(text):
    new_text = ""
    for word in re.split("_|-", text):
        if new_text == "":
            new_text = new_text + word
        else:
            new_text = new_text + word.capitalize()
    return new_text

print(to_camel_case(test1))
print(to_camel_case(test2))
