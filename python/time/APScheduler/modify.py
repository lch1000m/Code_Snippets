
import os.path, time, datetime
from dateutil import parser



def get_create_modified_time(file_path):
    """
    get creat & last modified time from given file_path
    """

    file_c = parser.parse(time.ctime(os.path.getctime(file_path)))
    file_m = parser.parse(time.ctime(os.path.getmtime(file_path)))

    return file_c, file_m



if __name__ == '__main__':

    file_path = r'C:\Codes\Snippets\sample data\aliasing.xlsx'

    c, m = get_create_modified_time(file_path)

    print(c)
    print(m)
