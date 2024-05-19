import logging
import os
import sys


class Logger:
    '''
    Logger class enables creation of  logger object in means of tracking events
    for trouble shooting when software runs.
    '''

    def __init__(self, name: str) -> None:
        '''
        Creates a logger object with a specified name.

        :param name: The specified name of the logger object.
        '''
        self.logger= logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        #stream out destination of log documents in 'save_logs_path' variable
        log_path= os.path.dirname(os.path.dirname(__file__))
        save_logs_path= os.path.join(log_path,'logs','out.log')

        #filehandler
        file_handler= logging.FileHandler(save_logs_path)
        file_handler.setLevel(logging.DEBUG)

        #streamhandler
        stream_handler= logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        #formatter
        formatter= logging.Formatter('%(levelname)s: %(asctime)s from %(name)s: %(process)s: %(funcName)s: %(lineno)s: %(message)s')

        #configure formatter & filehandler, streamhandler
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        #configure filehandler, streamhanlder to logger object
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def get_log(self) -> None:
        '''
        returns logger object
        '''
        return self.logger





if __name__ == '__main__':
    pass