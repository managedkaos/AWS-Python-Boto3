#!/usr/bin/env python
# a script to describe ec2 instances

# import the boto3 library
import boto3  

# create an EC2 resource
ec2 = boto3.resource('ec2')

# use the EC2 resource to iterate over all instances
# and print each instance ID and instance state
for instance in ec2.instances.all(): 
    print instance.id, instance.state
