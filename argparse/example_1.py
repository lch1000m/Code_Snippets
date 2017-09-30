# remove error rows

"""
reference
#
"""

import argparse

parser = argparse.ArgumentParser(description='명령행 인자를 쉽게 설정합시다.')
parser.add_argument("-i", "--input", type=int, required=True)  # foo라는 인자

args = parser.parse_args()

input = args.input


print('type: {0}, value: {1}'.format(type(input), input))
