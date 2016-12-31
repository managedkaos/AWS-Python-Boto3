#!/usr/bin/env python
# a script to create an rds instance

# import the boto3 library
import boto3

# create an rds client
rds = boto3.client('rds')

try:
    response = rds.create_db_instance(
        DBInstanceIdentifier='foo',
        DBName='yourdbname',
        MasterUsername='youruser',
        MasterUserPassword='yourpassword',
        DBInstanceClass='db.t2.micro',
        Engine='mariadb',
        AllocatedStorage=5)
    print response
except Exception as error:
    print error    