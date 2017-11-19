
# test for saving picture to local file

import urllib.request

url = 'https://3.bp.blogspot.com/-Bqe-I_Omsek/Wg7ZFjsW5BI/AAAAAAAAR8w/FrJCLfG9XB4WTGcVd8qj4uMSqW4LUfjWQCLcBGAs/s1600/000.jpg'

save_name = 'test.jpg'

urllib.request.urlretrieve(url, save_name)
