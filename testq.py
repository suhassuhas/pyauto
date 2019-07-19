def int2hex(number, bits=32):
    """ Return the 2'complement hexadecimal representation of a number """

    if number < 0:
        return hex((1 << bits) + number)
    else:
        return hex(number)


print(int2hex(-5))
