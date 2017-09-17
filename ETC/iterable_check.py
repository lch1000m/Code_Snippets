
"""
reference
# https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
"""

sample = [
    {'val1':1, 'val2':'abc'},
    [1,2,3],
    (1,2),
    'my name is earl',
    1,
    1.234,
]


# # 1st method
#
# for it in sample:
#     print('Contents : {0}'.format(it))
#     print('Item type: {0} & Iterable : {1}'.format(type(it), hasattr(it, '__iter__')))



# 2nd method

import collections

for it in sample:
    print('Contents : {0}'.format(it))
    print('Item type: {0} & Iterable : {1}'.format(type(it), isinstance(it, collections.Iterable)))


"""
result : 
>>>
Contents : {'val1': 1, 'val2': 'abc'}
Item type: <class 'dict'> & Iterable : True
Contents : [1, 2, 3]
Item type: <class 'list'> & Iterable : True
Contents : (1, 2)
Item type: <class 'tuple'> & Iterable : True
Contents : my name is earl
Item type: <class 'str'> & Iterable : True
Contents : 1
Item type: <class 'int'> & Iterable : False
Contents : 1.234
Item type: <class 'float'> & Iterable : False
>>>
"""
