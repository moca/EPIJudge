from test_framework import generic_test


def parity(x: int) -> int:
    """ The parity of a binary word is :
            - 1 is  is the number of ones is odd
            - 0 otherwise
    """
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
