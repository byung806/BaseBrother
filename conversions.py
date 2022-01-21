symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def convert_base(num: str, b1: int, b2: int) -> str:
    base10 = 0
    for c in num:
        base10 *= b1
        if (i := symbols.find(c)) == -1 or i > b1-1:
            return 'Invalid symbol'
        base10 += i
    
    result = ''
    while base10 != 0:
        result = symbols[base10 % b2] + result
        base10 = base10 // b2
    
    return result