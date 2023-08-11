import boto3

# create a custom session and set the profile name
session = boto3.Session(profile_name='matt-mcgivney')

# create the s3 resource client
s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)