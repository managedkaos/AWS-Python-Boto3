#!/usr/bin/env python
# a script to delete the contents of an s3 buckets

# import the sys and boto3 modules
import sys
import boto3

# create an s3 resource
s3 = boto3.resource('s3')

# iterate over the script arguments as bucket names
for bucket_name in sys.argv[1:]:

    # use the bucket name to create a bucket object
    bucket = s3.Bucket(bucket_name)

    # delete the bucket's contents and print the response or error
    for key in bucket.objects.all():
        try:
            response = key.delete()
            print response
        except Exception as error:
            print error
