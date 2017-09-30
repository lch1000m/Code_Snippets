# remove error rows

"""
reference
#
"""

def func1():
    print('function1 called!')


def func2():
    print('function2 called!')


def func3():
    print('function3 called!')



if __name__ == '__main__':

    import argparse

    _conv = {
        'func1': func12,
        'func2': func2,
        'func3': func3,
    }

    # new line added

    parser = argparse.ArgumentParser(description='명령행 인자를 쉽게 설정합시다.')
    parser.add_argument("-f", "--func", required=True)  # foo라는 인자

    args = parser.parse_args()

    func = args.func


    # _conv[func]()
    locals()[func]()
