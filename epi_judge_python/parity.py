from test_framework import generic_test


def parity(x: int) -> int:
    """ The parity of a binary word is :
            - 1 is  is the number of ones is odd
            - 0 otherwise
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
