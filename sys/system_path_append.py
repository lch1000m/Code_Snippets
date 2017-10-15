# functional path import

import subprocess, sys

paths = [
    r'C:\Codes\Snippets',
]

for path in paths:
    sys.path.append(path)

from example import test_pp


if __name__ == '__main__':

    test_pp()
