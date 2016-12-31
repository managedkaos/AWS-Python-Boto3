#!/usr/bin/env python
# a script to list buckets and their contents

# import the boto3 library
import boto3  

# create an S3 resource
s3 = boto3.resource('s3')

# list all buckets and their contents
for bucket in s3.buckets.all():
    print bucket.name
    print "---"
    for item in bucket.objects.all():
        print "\t%s" % item.key
