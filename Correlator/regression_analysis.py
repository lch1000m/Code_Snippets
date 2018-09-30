# demo for regression analysis

population = db.read(pop_option)    # read data from db
sample = db.read(sample_option)    # read data from db

pop_filter = Filter(pop_filter_option)  # generate filter class
population = filter.apply(pop_filter)   # adopt filter to data

path = Path_Info(path_option)
path.append_path(population)  # append path info to data

result = population.regression_analysis(correlation_option, target=sample)   # do one-way anova analysis
