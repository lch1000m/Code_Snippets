
import pickle
from pprint import pprint


def save_obj(obj, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':

    dic = {
        'task1': -1,
        'task2': -1,
        'task3': -1,
        'task4': -1,
    }

    save_obj(dic, 'res.txt')

    res = load_obj('res.txt')

    pprint(res)
