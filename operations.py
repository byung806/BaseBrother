from constants import get_base_symbols

def add(num1: str, num2: str, b: int) -> str:
    symbols = get_base_symbols(b)
    result = ''
    length = max(len(num1), len(num2))
    num1, num2 = (length*'0'+num1)[-length:], (length*'0'+num2)[-length:]
    carry = 0
    for i in range(-1, -len(num1)-1, -1):
        if (d1 := symbols.find(num1[i])) == -1 or (d2 := symbols.find(num2[i])) == -1:
            return 'Invalid Symbol'
        added = d1 + d2 + carry
        carry = added // b
        result = symbols[added % b] + result
    return result if carry == 0 else str(carry) + result


def subtract(num1: str, num2: str, b: int) -> str:
    symbols = get_base_symbols(b)
    result = ''
    length = max(len(num1), len(num2))
    num1, num2 = (length*'0'+num1)[-length:], (length*'0'+num2)[-length:]
    borrow = 0
    for i in range(-1, -len(num1)-1, -1):
        if (d1 := symbols.find(num1[i])) == -1 or (d2 := symbols.find(num2[i])) == -1:
            return 'Invalid Symbol'
        subtracted = d1 - d2 + borrow
        borrow = subtracted // b if subtracted < 0 else 0
        result = symbols[subtracted-borrow*b] + result
    return result if borrow == 0 else '-' + subtract(num2, num1, b)

print(subtract('AJKGLGAK', '1920ASGLSA', 36))