import os 
import sys
import traceback
import logging
from urllib.request import urlopen
import urllib.request

#configures python interpreter to find built-in modules and enable import statements
project_root= os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from utils.logger import Logger

#create logger object
_,filename= os.path.split(os.path.abspath(__file__))
_,dirname= os.path.split(_)
log_file_output= os.path.join(dirname,filename)
logger1= Logger(log_file_output)

#destination for data ingestion
dest_folder1: str= os.path.dirname(os.path.dirname(__file__))
dest_folder2: str= os.path.join(dest_folder1, 'i_data', 'external')
dest_path: str= f'{dest_folder2}/churn_data.csv'

#url
url: str= 'https://raw.githubusercontent.com/rolmez/Customer-Churn-Project/main/data/WA_Fn-UseC_-Telco-Customer-Churn.csv'


def download_url_data(url: str, destination_folder: str) -> None:
    if not os.path.exists(str(dest_folder2)):
        #create folder if it doesnt exist
        os.makedirs(str(dest_folder2))
    try:
        urllib.request.urlretrieve(url, dest_path)
        logger1.get_log().info(f'csv file downloaded successfully to {dest_folder2}')
    except Exception as e:
        logger1.get_log().error(f'Error while downloading the csv file due to: {e}')
        traceback.print_exc()


def main():
    download_url_data(url, dest_folder2)


if __name__ == '__main__':
    main()