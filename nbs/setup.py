"""
After changing your working directory in `config.py`, run this IE python setup.py
"""

import os
from tqdm import tqdm
import s3
import config

s3_files = s3.ls(config.RAW_TWEETS_S3 + '*.json.bz2')
print("downloading raw tweets...")
for f in tqdm(s3_files):
    local_f = os.path.join(config.RAW_TWEETS_DIRECTORY, 
                           os.path.basename(f))
    s3.wget(f, local_f)
    
s3_files = s3.ls(config.INTERMERDAITE_S3 + '*')
print("downloading intermediate files...")
for f in tqdm(s3_files):
    local_f = os.path.join(config.INTERMEDIATE_DIRECTORY, 
                           os.path.basename(f))
    s3.wget(f, local_f)