# db class hierarchy


db_option = {
    'db': 'yms',
    'type': 'il',
}



class DB(object):

    def __init__(self, option):
        # initializing option contents

        default_option = default_option   # load default option
        option = default_option.update(option)

        self.option = option


    def read(self):
        # read data from db
        pass
