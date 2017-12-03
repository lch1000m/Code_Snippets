
from func import write_replace_html_contents


replace_values = {
    'title': {'tag':'title', 'attrs':{}, 'replace_value':'new title!'},
    'sect1': {'tag':'div', 'attrs':{'id':'1st'}, 'replace_value':'new val1!'},
    'sect2': {'tag':'div', 'attrs':{'id':'2nd'}, 'replace_value':'new val2!'},
    'sect3': {'tag':'div', 'attrs':{'id':'3rd'}, 'replace_value':'new val3!'},
}



res = write_replace_html_contents('psutil.html', replace_values=replace_values, write_to='output.html')

print(type(res))
print(res)
