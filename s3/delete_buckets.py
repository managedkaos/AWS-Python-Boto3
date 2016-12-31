#!/usr/bin/env python
# a script to delete s3 buckets
# bucket must be empty before it can be deleted!

# import the sys and boto3 modules
import sys
import boto3

# create an s3 resource
s3 = boto3.resource('s3')

# iterate over the script arguments as bucket names
for bucket_name in sys.argv[1:]:

    # use the bucket name to create a bucket object
    bucket = s3.Bucket(bucket_name)

    # delete the bucket and print the response or error
    try:
        response = bucket.delete()
        print response
    except Exception as error:
        print error
