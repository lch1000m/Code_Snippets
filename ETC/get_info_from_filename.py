

def get_info_from_name(filename):

    if ',' in filename:
        _temp = filename.split(' ', 1)

        db_name = _temp[0]

        __temp = _temp[1].split(',')

        time = __temp[0]

        file_source = __temp[1].strip()

        return db_name, time, file_source

    else:
        _temp = filename.split(' ', 1)

        db_name = _temp[0]

        time = _temp[1].split('.')[0]

        return db_name, time




if __name__ == '__main__':

    # filename = 'IL 2017-10-20 08:50:21, data.csv'
    filename = 'IL 2017-10-20 08:50:21.csv'


    res = get_info_from_name(filename)


    print(res)
