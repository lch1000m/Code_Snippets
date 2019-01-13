# inline trend analysis

data = DB(input_option).read()    # read data from db

filter = Filter(filter_option)  # generate filter class
data = filter.apply(data)   # adopt filter to data

alais = Filter(alias_option)  # generate filter class
data = alais.apply(data)   # adopt filter to data

path = Path_Info(path_option)
path.append_path(data)  # append path info to data
