"""
The rgb function is incomplete. Complete it so that passing in RGB 
decimal values will result in a hexadecimal representation being 
returned. Valid decimal values for RGB are 0 - 255. Any values 
that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand 
with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""

def Num_to_hex(number):
    Hex_table = ['0','1','2','3','4','5','6','7','8','9',
    'A','B','C','D','E','F']
    if number > 255:
        first = round(255/16,2)
        print('too big')
    elif number < 0:
        first = round(0/16,2)
        print ('too small')
    else:
        first = round(number/16,2)
        print('just right')
    first_A = Hex_table[int(first)]
    first_B = Hex_table[round((first - int(first))*16)]
    return first_A, first_B

def rgb(r, g, b):
    Hex = ""
    Hex = Hex + "{}{}".format(Num_to_hex(r)[0], Num_to_hex(r)[1] )
    Hex = Hex + "{}{}".format(Num_to_hex(g)[0], Num_to_hex(g)[1] )
    Hex = Hex + "{}{}".format(Num_to_hex(b)[0], Num_to_hex(b)[1] )
    print(Hex)
    return Hex

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
