import os

# What local directory do you want to read and write data to?
WORKING_DIRECTORY = 'data/' # change this!

# where public s3 data is stored
RAW_TWEETS_S3 = 's3://smapp-nyu-public/links-as-data/tweets-raw'
INTEMEDIATE_S3 =  's3://smapp-nyu-public/links-as-data/processed-data'


# don't change this! we're going to create the directories we work with.
RAW_TWEETS_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'tweets-raw')
INTERMEDIATE_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'processed-data')
for directory in [WORKING_DIRECTORY, RAW_TWEETS_DIRECTORY, INTERMEDIATE_DIRECTORY]:
    os.makedirs(directory, exist_ok=True)