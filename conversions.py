from constants import get_base_symbols

def convert_base(num: str, b1: int, b2: int) -> str:
    symbols = get_base_symbols(b1)
    base10 = 0
    for c in num:
        base10 *= b1
        if (i := symbols.find(c)) == -1:
            return 'Invalid Symbol'
        base10 += i
    
    symbols = get_base_symbols(b2)
    result = ''
    while base10 != 0:
        result = symbols[base10 % b2] + result
        base10 = base10 // b2
    
    return result