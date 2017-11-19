
import urllib.request


url = 'https://www.youtube.com/watch?v=Lts0Z9o94zk&index=2&list=PL51JScfFH339kZBfI-vxuNuwCpE1P7SIs'

res = urllib.request.urlopen(url)

data = res.read()

text = data.decode('utf-8')

print(text)
