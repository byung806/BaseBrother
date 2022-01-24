from constants import symbols_2_63, symbols_64

def convert_base(num: str, b1: int, b2: int) -> str:
    if b1 >= 2 and b1 <= 63:
        symbols = symbols_2_63
    elif b1 == 64:
        symbols = symbols_64
    else:
        symbols = ' '*1000
    base10 = 0
    for c in num:
        base10 *= b1
        if (i := symbols.find(c)) == -1 or i > b1-1:
            return 'Invalid symbol'
        base10 += i
    
    if b2 >= 2 and b2 <= 63:
        symbols = symbols_2_63
    elif b2 == 64:
        symbols = symbols_64
    else:
        symbols = ' '*1000

    result = ''
    while base10 != 0:
        result = symbols[base10 % b2] + result
        base10 = base10 // b2
    
    return result