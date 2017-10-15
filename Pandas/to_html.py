# to_html

import pandas as pd


dic = {
    ('',''):[0,1,2],
    ('Header', 'sub1'):[1,2,3],
    ('Header', 'sub2'):[4,5,6],
    ('Contents','sub1'):['a','b','c'],
    ('Contents','sub1'):['d','e','f'],
}


df = pd.DataFrame(dic)

df_html = df.to_html(index=False)

with open('test.html', 'w') as file:
    file.write(df_html)
