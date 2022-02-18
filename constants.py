symbols_2_63 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
symbols_64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def get_base_symbols(base: int) -> str:
    if base < 2:
        return ''
    elif base < 64:
        return symbols_2_63[:base]
    elif base == 64:
        return symbols_64
    else:
        return ''