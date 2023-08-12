from utils import get_date
import boto3.exceptions
import logging

def upload_file(s3_client, file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    
    object_name = get_date() + '/' + object_name

    # Upload the file
    try:
        s3_client.Object(bucket, object_name).upload_file(file_name)
    except boto3.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True