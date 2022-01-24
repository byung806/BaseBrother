from constants import symbols_2_63, symbols_64

def add(num1: str, num2: str, b: int) -> str:
    if b >= 2 and b <= 63:
        symbols = symbols_2_63
    elif b == 64:
        symbols = symbols_64
    else:
        symbols = ' '*1000
    result = ''
    length = max(len(num1), len(num2))
    num1, num2 = (length*'0'+num1)[-length:], (length*'0'+num2)[-length:]
    carry = 0
    for i in range(-1, -len(num1)-1, -1):
        added = symbols.find(num1[i]) + symbols.find(num2[i]) + carry
        carry = added // b
        result = symbols[added % b] + result
    return result if carry == 0 else str(carry) + result


def subtract(num1: str, num2: str, b: int) -> str:
    if b >= 2 and b <= 63:
        symbols = symbols_2_63
    elif b == 64:
        symbols = symbols_64
    else:
        symbols = ' '*1000
    result = ''
    length = max(len(num1), len(num2))
    num1, num2 = (length*'0'+num1)[-length:], (length*'0'+num2)[-length:]
    borrow = 0
    for i in range(-1, -len(num1)-1, -1):
        subtracted = symbols.find(num1[i]) - symbols.find(num2[i]) + borrow
        borrow = subtracted // b if subtracted < 0 else 0
        result = symbols[subtracted-borrow*b] + result
    return result if borrow == 0 else '-' + subtract(num2, num1, b)

print(subtract('AJKGLGAK', '1920ASGLSA', 36))