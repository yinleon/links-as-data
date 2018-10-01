import os

# What local directory do you want to read and write data to?
WORKING_DIRECTORY = 'data/' # change this!

# DON'T CHANGE BELOW

# where public s3 data is stored
RAW_TWEETS_S3 = 's3://smapp-nyu-public/links-as-data/tweets-raw.tar.bz2'
INTERMEDIATE_S3 = 's3://smapp-nyu-public/links-as-data/processed-data/'
CONGRESS_METADATA_S3 = 's3://smapp-nyu-public/links-as-data/congress/'

# don't change this! we're going to create the directories we work with.
RAW_TWEETS_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'tweets-raw')
INTERMEDIATE_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'processed-data')
CONGRESS_METADATA_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'congress')
for directory in [WORKING_DIRECTORY, RAW_TWEETS_DIRECTORY, INTERMEDIATE_DIRECTORY, CONGRESS_METADATA_DIRECTORY ]:
    os.makedirs(directory, exist_ok=True)