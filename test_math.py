#!/usr/bin/env python

def custom_sum(a, b):
    """Calculate the sum of two given numbers."""
    return a + b

if __name__ == '__main__':
    a = 2
    b = 3
    print '%d + %d = %d' % (a, b, custom_sum(a, b))
