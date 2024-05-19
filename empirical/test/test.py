import os
import sys

project_root= os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from utils.logger import Logger

_, file_name= os.path.split(__file__)
_, dir_name= os.path.split(_)

log_file_output= os.path.join(dir_name,file_name)
logger1= Logger(log_file_output)



