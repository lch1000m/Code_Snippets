# dictionary key existence check in hierarchical dictionary

"""
reference
# https://stackoverflow.com/questions/16003408/python-dict-get-with-multidimensional-dict
"""


dic = {
    'val1': {
        'sub_val1':1,
        'sub_val2':1.1111,
    },
    'val2': 1,
    'val3': 123.45,
}

# # 1 dimensional
# res = dic.get('val1', None) or 'attr error'

# 2 dimensional
res = dic.get('val1', {}).get('sub_val3', None) or 'error'

print(res)
