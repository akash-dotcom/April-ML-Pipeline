from datetime import datetime
import logging
import os,sys

LOG_DIR="logs"
CURRRENT_TIME_STAMP=f"log{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

log_file_name=f"logs{CURRRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

log_file_path=os.path.join(LOG_DIR,log_file_name)

logging.basicConfig(filename=log_file_path,
                     filemode="w",
                      format='[%(asctime)s] %(name)s - %(levelname)s-%(message)s',
                      level=logging.INFO
                      )