#!/usr/bin/env python
# a script to create an ec2 instance

# import the boto3 library
import boto3

# create an EC2 resource
ec2 = boto3.resource('ec2')

# use the EC2 resource to create an instance
instance = ec2.create_instances(
    #ImageId='INSTERT-AMI-ID-HERE', 
    ImageId='ami-1e299d7e', 
    MinCount=1, 
    MaxCount=1, 
    InstanceType='t2.micro')

# print the instance ID 
print instance[0].id
