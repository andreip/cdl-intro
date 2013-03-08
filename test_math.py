#!/usr/bin/env python

def custom_sum(*args):
    """Calculate the sum of two given numbers.
       Make the sum work for multiple arguments
    """
    crt = 1
    for var in args:
        crt += var
    return crt

if __name__ == '__main__':
    a = 2
    b = 3
    print '%d + %d = %d' % (a, b, custom_sum(a, b))
