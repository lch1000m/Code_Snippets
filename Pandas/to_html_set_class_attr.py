
import pandas as pd


df = pd.DataFrame(
    {
        'A':[1,2,3],
        'B':['a','b','c'],
    }
)


html = df.to_html(index=False, classes='table1')

html2 = df.to_html(index=False, classes='table2')

res = html + html2


print(res)
