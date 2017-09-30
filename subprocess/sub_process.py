
import argparse, time

parser = argparse.ArgumentParser(description='명령행 인자를 쉽게 설정합시다.')
parser.add_argument("-i", "--input", required=True)  # foo라는 인자

args = parser.parse_args()

input = args.input


while True:

    print('{0} called!'.format(input))

    time.sleep(1)
