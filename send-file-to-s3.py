from botocore.exceptions import ClientError
import boto3
import configparser

# read some config values
config = configparser.ConfigParser()
config.read('app.cfg')

# create a custom session and set the profile name
session = boto3.Session(profile_name=config['app-config']['PROFILE_NAME'])

# create the s3 resource client
s3 = session.resource('s3')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    
    # Upload the file
    s3.Object(bucket, object_name).upload_file(file_name)

with open(config['app-config']['FILE_NAME'], "rb") as f:
    upload_file(config['app-config']['FILE_NAME'], config['app-config']['BUCKET_NAME'], config['app-config']['OBJECT_NAME'])    