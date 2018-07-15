
import pandas as pd

def convert_int_to_2digit_str(input):

    res = []

    for inp in input:
        if inp > 10:
            res.append(str(inp))
        else:
            res.append('0' + str(inp))

    return res



input = [1,2,3,15]

res = convert_int_to_2digit_str(input)

print(res)
