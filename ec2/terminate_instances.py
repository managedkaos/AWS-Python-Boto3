#!/usr/bin/env python
# a script to terminate ec2 instances

# import the sys and boto3 modules
import sys
import boto3

# create an EC2 resource
ec2 = boto3.resource('ec2')

# iterate over the script arguments as instance IDs
for instance_id in sys.argv[1:]:
    
    # create an object to manipulate the instance with the given ID
    instance = ec2.Instance(instance_id)

    # terminate the instance; capture and print the response
    response = instance.terminate()
    print response
