"""
ROT13 is a simple letter substitution cipher that replaces a 
letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string 
ciphered with Rot13. If there are numbers or special characters 
included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
"""

def rot13(message):
    cipher = ""
    for letter in message:
        number = ord(letter)
        #upper case letters
        if 65 <= number <= 90:
            if number + 13 > 90:  Convert = chr(number - 13)
            else:  Convert = chr(number + 13)
            cipher += Convert

        #lower case letters
        elif 97 <= number <= 122:
            if number + 13 > 122:  Convert = chr(number - 13)
            else:  Convert = chr(number + 13)
            cipher += Convert

        #not a letter
        else:
            cipher += letter

    print(cipher)
    return cipher

rot13("test")
rot13("Test")
