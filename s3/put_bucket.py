#!/usr/bin/env python
# a script to put a file into an s3 bucket

# import the sys and boto3 modules
import sys
import boto3

# create an S3 resource
s3 = boto3.resource("s3")

# get the bucket and file names from the arguments
bucket_name = sys.argv[1]
object_name = sys.argv[2]

# upload the file to the bucket and print the response or error
try:    
    response = s3.Object(bucket_name, object_name).put(Body=open(object_name, 'rb'))
    print response
except Exception as error:
    print error
