import boto3
import configparser
from upload_file import upload_file

# read some config values
config = configparser.ConfigParser()
config.read('app.cfg')

# create a custom session and set the profile name
session = boto3.Session(profile_name=config['app-config']['PROFILE_NAME'])

# create the s3 resource client
s3 = session.resource('s3')

# upload the file
with open(config['app-config']['FILE_NAME'], "rb") as f:
    upload_file(s3, config['app-config']['FILE_NAME'], config['app-config']['BUCKET_NAME'])
    print("File uploaded successfully")