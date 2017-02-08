#!/usr/bin/env python
# a script to create an s3 bucket

# import the sys and boto3 modules
import sys
import boto3

# create an s3 resource
s3 = boto3.resource("s3")

# iterate over the script arguments as bucket names
for bucket_name in sys.argv[1:]:

    # create the bucket and print the response or error
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        print response
    except Exception as error:
        print error
